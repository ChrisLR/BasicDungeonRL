from bflib import dice
from bflib.characters.specialabilities import OpenLock as OpenLockAbility
from core.abilities.base import Ability
from core.components import Lock
from services import echo, selection
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

    @classmethod
    def can_execute(cls, character, target_selection=None):
        if not target_selection:
            return False

        lock = target_selection[0].lock
        if not lock or not lock.locked:
            return False

        if target_selection[0].lock.has_failed(character):
            echo.player_echo(
                character, "You can not make another attempt this level.")
            return False

        if character.query.special_ability(OpenLockAbility) <= 0:
            return False

        return True

    @classmethod
    def execute(cls, character, target_selection=None):
        open_lock_target = character.query.special_ability(OpenLockAbility)
        item = target_selection[0]
        value = dice.D100(1).roll()
        if value > open_lock_target:
            echo.see(
                actor=character,
                actor_message="You fail at picking {}'s lock!"
                              "".format(item.name),
                observer_message="{} fails at picking {}'s lock!"
                                 "".format(character.name, item.name)
            )
            item.lock.add_failed_attempt(character, character.experience.level)
            return False
        else:
            item.lock.unlock()
            echo.see(
                actor=character,
                actor_message="You succeed in picking {}'s lock!"
                              "".format(item.name),
                observer_message="{} succeeds in picking {}'s lock!"
                                 "".format(character.name, item.name)
            )

        return True
