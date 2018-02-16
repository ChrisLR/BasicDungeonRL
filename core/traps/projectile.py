from bflib import traps as base_traps
from core.traps.base import Trap


class Projectile(Trap):
    def trigger(self, event):
        origin_target = event.actor
        targets = self._retrieve_targets(origin_target)
        for target in targets:
            successful_hit = self._make_attack(target)
            if successful_hit:
                self._apply_effect(target)

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
                target.effects.add_base_effect(base_effect)

    @classmethod
    def _make_attack(cls, target):
        """
        This would launch an attack against the target.
        Applying damage if needed
        :returns: True if Touched, False if not
        """
        return True

    @classmethod
    def _retrieve_targets(cls, origin_target):
        """
        This would use the base target type to retrieve all targets.
        Using the Triggering Target as Origin
        """
        return [origin_target]


class Arrow(Projectile):
    base_trap = base_traps.Arrow
