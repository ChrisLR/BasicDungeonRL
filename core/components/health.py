from core.components.base import Component


class Health(Component):
    NAME = 'health'

    def __init__(self, hit_dice=None, first_enforced_maximum=False):
        super().__init__()
        if hit_dice:
            self.update_hit_dice(hit_dice)
            self.current = self.max
        self.first_enforced_maximum = first_enforced_maximum
        self._hit_dices = {}
        self._health_rolls = []
        self.current = 0
        self._base_max_health = 0
        self.maximum_modifiers = []

    @property
    def largest_hit_dice(self):
        largest_hit_dice = max(self._hit_dices.values(), key=lambda h: h.amount)
        return largest_hit_dice

    @property
    def total_hit_dice_value(self):
        return sum(hit_dice.amount for hit_dice in self._hit_dices.values())

    def update_hit_dice(self, new_hit_dice):
        current_hit_dice = self._hit_dices[type(new_hit_dice)]
        if not self._hit_dices:
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
                        roll = new_hit_dice.roll(1, new_hit_dice.flat_bonus)
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
        if self.host.experience_pool:
            level = self.host.experience_pool.total_level
        else:
            level = 1

        if self.host.stats:
            constitution_bonus = self.host.stats.constitution.modifier
        else:
            constitution_bonus = 0

        return self._base_max_health + sum(self.maximum_modifiers) + (constitution_bonus * level)

    def register_modifier(self, health_modifier):
        self.maximum_modifiers.append(health_modifier)

    def unregister_modifier(self, health_modifier):
        self.maximum_modifiers.remove(health_modifier)

    def on_register(self, host):
        if host.experience_pool:
            level = host.experience_pool.total_level
        else:
            level = 1

        if host.character_class:
            hit_die = host.character_class.get_hit_dice(level)
        else:
            hit_die = 0

        self.update_hit_dice(hit_die)
        self.current = self.max

    def copy(self):
        new = Health(self.first_enforced_maximum)
        new.update_hit_dice(self.largest_hit_dice)
        return new
