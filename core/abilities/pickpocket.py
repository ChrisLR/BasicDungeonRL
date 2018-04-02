from bflib import dice
from bflib.characters.specialabilities import PickPockets as PickPocketAbility
from core import components
from core.abilities.base import Ability
from services import echo
from services import selection
from services.selection import filters, TargetSelectionSet, TargetSelectionChain


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

    @classmethod
    def execute(cls, character, target_selection=None):
        holder = target_selection.get("Holder")
        item = target_selection.get("Item")
        pick_pocket_target = character.query.special_ability(PickPocketAbility)
        value = dice.D100(1).roll()

        if value > pick_pocket_target:
            if value == 100 or value >= pick_pocket_target * 2:
                echo.see(
                    actor=character,
                    actor_message="{} catches you trying to steal!".format(holder.name),
                    observer_message="{} catches {} trying to steal!".format(
                        echo.name_or_you(holder),
                        character.name,
                    )
                )
            else:
                echo.player_echo(
                    actor=character,
                    message="You fail your pick pocket attempt!"
                )

            return False
        else:
            if holder.inventory.remove(item):
                if character.inventory.add(item):
                    echo.player_echo(
                        character, "You steal {} from {} !".format(item.name, holder.name))
                else:
                    holder.inventory.add(item)
                    echo.player_echo(
                        character, "You are too full to steal {} from {} !".format(item.name, holder.name))
        return True
