from core.actions.base import Action
from services import selection
from services.selection import filters
from core.messaging import StringBuilder, Verb, Actor, Target
from core import contexts


class Put(Action):
    name = "put"
    target_selection = selection.TargetSelectionChain(
        selection.TargetSelectionSet(
            name="Container",
            selections=selection.DirectionalSelection,
            filters=(
                filters.TileExclusion,
                filters.SingleHierarchy
            )
        ),
        selection.TargetSelectionSet(
            name="Content",
            selections=selection.AllItems,
            filters=(
                filters.TileExclusion,
                filters.Hierarchy
            )
        )
    )

    def can_execute(self, character, target_selection=None):
        if not character.equipment and not character.inventory:
            return False

        if not target_selection:
            return False

        container_object = target_selection.get("Container").targets[0]
        if not container_object or not container_object.container:
            return

        if container_object.openable and container_object.openable.closed:
            if container_object.lock and container_object.lock.locked:
                self.game.echo.player(character, "You cant do that, {} is locked.".format(container_object.name))
                return False

        if not target_selection.get("Content"):
            return False

        return True

    def execute(self, character, target_selection=None):
        if not target_selection:
            return False

        container_object = target_selection.get("Container").targets[0]
        container = container_object.container
        content = target_selection.get("Content")

        for game_object in content:
            if not character.equipment.remove(game_object) and not character.inventory.remove(game_object):
                self.game.echo.player(character, "You cant drop {}".format(game_object.name))
                continue

            if not container.add_item(game_object):
                self.game.echo.player(
                    actor=character,
                    message="You cant put {} in {}".format(game_object.name, container_object.name))
                continue

            target_level = game_object.location.level
            if target_level:
                target_level.remove_object(game_object)

            context = contexts.Action(actor=character, target=container_object)
            message = StringBuilder(Actor, Verb("put", Actor), "in", Target)
            self.game.echo.see(character, message, context)

        return True
