from bflib import dice
from bflib.characters.specialabilities import OpenLock as OpenLockAbility
from core import contexts
from core.abilities.base import Ability
from core.components import Lock
from messaging import StringBuilder, Actor, Verb, Target
from services import selection
from services.selection import filters


class OnlyWithLocks(filters.Component):
    component = Lock

    def filter(self, targets):
        self.resolution = [
            target for target in targets
            if target.lock and target.lock.locked
        ]


class OpenLock(Ability):
    name = "Open Lock"
    target_selection = selection.TargetSelectionSet(
        selections=selection.DirectionalSelection,
        filters=(OnlyWithLocks, filters.SingleListBased))

    def can_execute(self, character, target_selection=None):
        if not target_selection:
            return False

        lock = target_selection[0].lock
        if not lock or not lock.locked:
            return False

        if target_selection[0].lock.has_failed(character):
            self.game.echo.player(character, "You can not make another attempt this level.")

            return False

        if character.query.special_ability(OpenLockAbility) <= 0:
            return False

        return True

    def execute(self, character, target_selection=None):
        open_lock_target = character.query.special_ability(OpenLockAbility)
        item = target_selection[0]
        value = dice.D100(1).roll_total()
        if value > open_lock_target:
            context = contexts.Action(character, item)
            message = StringBuilder(Actor, Verb("fail", Actor), "at picking", Target, "'s lock!")
            self.game.echo.see(
                actor=character,
                message=message,
                context=context
            )
            item.lock.add_failed_attempt(character, character.experience.level)

            return False

        item.lock.unlock()
        context = contexts.Action(character, item)
        message = StringBuilder(Actor, Verb("succeed", Actor), "at picking", Target, "'s lock!")
        self.game.echo.see(
            actor=character,
            message=message,
            context=context
        )

        return True
