from bflib import dice
from bflib.characters.specialabilities import OpenLock as OpenLockAbility
from core import components
from core.abilities.base import Ability
from services import echo
from services.selection import DirectionalSelection, filters, TargetSelectionSet


class OnlyWithLocks(filters.Component):
    component = components.Lock


class OpenLock(Ability):
    name = "Open Lock"
    target_selection = TargetSelectionSet(
        selections=DirectionalSelection,
        filters=(OnlyWithLocks, filters.SingleListBased))

    @classmethod
    def can_execute(cls, character, target_selection=None):
        if not target_selection or not target_selection[0].lock:
            return False

        if target_selection[0].lock.has_failed(character):
            if echo.is_player(character):
                echo.echo_service.echo("You can not make another attempt this level.")
            return False

        if character.query.special_ability(OpenLockAbility) <= 0:
            return False

        return True

    @classmethod
    def execute(cls, character, target_selection=None):
        open_lock_value = character.query.special_ability(OpenLockAbility)
        item = target_selection[0]
        value = dice.D100(1).roll()
        if value > open_lock_value:
            if echo.is_player(character):
                echo.echo_service.echo(
                    "You fail at picking {}'s lock!".format(item.name))
            else:
                echo.echo_service.echo(
                    "{} fails at picking {}'s lock!".format(character.name, item.name))
            item.lock.add_failed_attempt(character, character.experience.level)
            return False
        else:
            item.lock.unlock()
            if echo.is_player(character):
                echo.echo_service.echo(
                    "You succeed in picking {}'s lock!".format(item.name))
            else:
                echo.echo_service.echo(
                    "{} succeeds in picking {}'s lock!".format(character.name, item.name))
        return True
