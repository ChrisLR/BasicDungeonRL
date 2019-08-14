from bfgame.attacks.ranged import RangedAttack
from bfgame.effects import get_core_effect_from_base
from bflib import traps as base_traps
from core.traps.base import Trap


class Projectile(Trap):
    @classmethod
    def on_trigger_echo(cls, host, origin_target):
        pass

    @classmethod
    def on_hit_echo(cls, host, target, total_damage):
        pass

    @classmethod
    def on_miss_echo(cls, host, target):
        pass

    @classmethod
    def trigger(cls, host, event):
        origin_target = event.actor
        targets = cls._retrieve_targets(origin_target)
        cls.on_trigger_echo(host, origin_target)
        for target in targets:
            successful_hit = cls._make_attack(host, target)
            if successful_hit:
                cls._apply_effect(target)

    @classmethod
    def _apply_effect(cls, target):
        """
        Applies the effect defined to the target, if any.
        """
        base_effect = cls.base_trap.effect
        if base_effect is not None:
            saving_throw = cls.base_trap.saving_throw
            if saving_throw and target.savingthrows:
                saved = target.savingthrows.make(saving_throw)
            else:
                saved = False

            if not saved:
                target.effects.add_effect(get_core_effect_from_base(base_effect))

    @classmethod
    def _make_attack(cls, host, target):
        """
        This would launch an attack against the target.
        Applying damage if needed
        :returns: True if Touched, False if not
        """
        # TODO Traps are broken
        attack = RangedAttack(cls.base_trap.attack, host, target)
        attack.execute(host, target, cls.base_trap, )
        if attack.total_damage:
            target.health.take_damage(attack.total_damage)
            cls.on_hit_echo(host, target, attack.total_damage)
            return True
        else:
            cls.on_miss_echo(host, target)
            return False

    @classmethod
    def _retrieve_targets(cls, origin_target):
        """
        This would use the base target type to retrieve all targets.
        Using the Triggering Target as Origin
        """
        return [origin_target]


class Arrow(Projectile):
    base_trap = base_traps.Arrow

    @classmethod
    def on_trigger_echo(cls, host, origin_target):
        echo = host.game.echo
        actor_message = "Your trap shoots an arrow towards {}!".format(origin_target.name)
        observer_message = "An arrow shoots from {} towards {}!".format(
            origin_target.name, origin_target.name
        )
        target_message = "An arrow shoots from {} towards you!".format(origin_target.name)
        echo.see_m(
            actor=host,
            target=origin_target,
            actor_message=actor_message,
            observer_message=observer_message,
            target_message=target_message
        )

    @classmethod
    def on_hit_echo(cls, host, target, total_damage):
        echo = host.game.echo
        actor_message = "It hits {} for {} damage!".format(target.name, total_damage)
        target_message = "It hits you for {} damage!".format(total_damage)
        echo.see(
            actor=host,
            target=target,
            actor_message=actor_message,
            observer_message=actor_message,
            target_message=target_message
        )

    @classmethod
    def on_miss_echo(cls, host, target):
        echo = host.game.echo
        actor_message = "It misses {}!".format(target.name)
        target_message = "It misses you!"
        echo.see(
            actor=host,
            target=target,
            actor_message=actor_message,
            observer_message=actor_message,
            target_message=target_message
        )
