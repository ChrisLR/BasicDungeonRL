from core.components.base import Component


class Health(Component):
    NAME = 'health'
    __slots__ = ["first_enforced_maximum", "_hit_dices", "_health_rolls",
                 "current", "_base_Max_health", "maximum_modifiers", "dead"]

    def __init__(self, first_enforced_maximum=False):
        super().__init__()
        self.first_enforced_maximum = first_enforced_maximum
        self._hit_dices = {}
        self._health_rolls = []
        self.current = 0
        self._base_max_health = 0
        self.maximum_modifiers = []
        self.dead = False

    @property
    def largest_hit_dice(self):
        largest_hit_dice = max(self._hit_dices.values(), key=lambda h: h.amount)
        return largest_hit_dice

    @property
    def total_hit_dice_value(self):
        return sum(hit_dice.amount for hit_dice in self._hit_dices.values())

    def revive(self, health_recovered=1):
        if self.dead:
            self.dead = False
            self.current = health_recovered if health_recovered <= self.max else self.max

    def restore_health(self, health):
        if not self.dead:
            self.current += health

    def take_damage(self, damage):
        self.current -= damage
        if self.current <= 0:
            self.dead = True

    def update_hit_dice(self, new_hit_dice):
        current_hit_dice = self._hit_dices.get(type(new_hit_dice), None)
        if not current_hit_dice:
            self._hit_dices[type(new_hit_dice)] = new_hit_dice
            if self.first_enforced_maximum:
                self._base_max_health = new_hit_dice.sides * new_hit_dice.amount
            else:
                self._base_max_health = new_hit_dice.roll()
        else:
            if type(new_hit_dice) in self._hit_dices:
                delta_amount = new_hit_dice.amount - current_hit_dice.amount
                if delta_amount > 0:
                    health_gain = 0
                    for i in range(0, delta_amount):
                        roll = new_hit_dice.manual_roll(1, new_hit_dice.flat_bonus)
                        health_gain += roll
                        self._health_rolls.append(roll)

                    self._base_max_health += health_gain
                    self.current += health_gain
                else:
                    health_loss = 0
                    for roll in range(0, abs(delta_amount)):
                        health_loss += self._health_rolls.pop(-1)
                    self._base_max_health -= health_loss
                    if self.current > 0 and self.current - health_loss <= 0:
                        self.current = 1
                    else:
                        self.current -= health_loss
                    self._hit_dices[type(new_hit_dice)] = new_hit_dice

    @property
    def max(self):
        if self.host.experience:
            level = self.host.experience.level
        else:
            level = 1

        if self.host.stats:
            constitution_bonus = self.host.stats.constitution_modifier
        else:
            constitution_bonus = 0

        return self._base_max_health + sum(self.maximum_modifiers) + (constitution_bonus * level)

    def register_modifier(self, health_modifier):
        self.maximum_modifiers.append(health_modifier)

    def unregister_modifier(self, health_modifier):
        self.maximum_modifiers.remove(health_modifier)

    def on_register(self, host):
        super().on_register(host)
        if host.experience:
            level = host.experience.level
        else:
            level = 1

        if host.character_class:
            hit_die = host.character_class.get_hit_dice(level)
        else:
            hit_die = 0

        if host.monster:
            hit_die = host.monster.base_monster.hit_dice

        self.update_hit_dice(hit_die)
        self.current = self.max

    def copy(self):
        new = Health(self.first_enforced_maximum)
        new.update_hit_dice(self.largest_hit_dice)
        return new
