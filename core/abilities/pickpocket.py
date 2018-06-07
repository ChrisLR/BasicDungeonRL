from bflib import dice
from bflib.characters.specialabilities import PickPockets as PickPocketAbility
from core.abilities.base import Ability
from core import contexts
from services import selection
from services.selection import filters, TargetSelectionSet, TargetSelectionChain
from messaging import StringBuilder, Actor, Verb, TargetOne, TargetTwo


class PickPocket(Ability):
    name = "Pick Pocket"
    target_selection = TargetSelectionChain(
        TargetSelectionSet(
            selections=selection.DirectionalSelection,
            filters=(filters.ExcludeItemFlags, filters.SingleListBased),
            name="Holder"
        ),
        TargetSelectionSet(
            selections=selection.ChainedInventory,
            filters=filters.SingleListBased,
            name="Item",
        )
    )

    @classmethod
    def can_execute(cls, character, target_selection=None):
        if not target_selection:
            return False

        if not target_selection.get("Holder"):
            return False

        if not target_selection.get("Item"):
            return False

        if character.query.special_ability(PickPocketAbility) <= 0:
            return False

        return True

    def execute(self, character, target_selection=None):
        holder = target_selection.get("Holder")
        item = target_selection.get("Item")
        pick_pocket_target = character.query.special_ability(PickPocketAbility)
        value = dice.D100(1).roll_total()
        context = contexts.TwoTargetAction(character, holder, item)
        if value > pick_pocket_target:
            if value == 100 or value >= pick_pocket_target * 2:
                message = StringBuilder(TargetOne, Verb("catch", TargetOne), Actor, "trying to steal")
                self.game.echo.see(character, message, context)
            else:
                self.game.echo.player(character, "You fail your pick pocket attempt!")

            return False
        else:
            if holder.inventory.remove(item):
                if character.inventory.add(item):
                    message = StringBuilder(Actor, Verb("steal", Actor), TargetTwo, "from", TargetOne)
                    self.game.echo.player(character, message)
                else:
                    holder.inventory.add(item)
                    message = StringBuilder(Actor, "are too full to steal", TargetTwo, "from", TargetOne, "!")
                    self.game.echo.player(character, message)

        return True
