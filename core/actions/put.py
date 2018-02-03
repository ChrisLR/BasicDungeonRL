from core.actions.base import Action
from services import selection
from services.selection import filters


class Put(Action):
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

    @classmethod
    def can_execute(cls, character, selection=None):
        if not character.equipment and not character.inventory:
            return False

        if not selection:
            return False

        container_object = selection.get("Container")
        if not container_object or not container_object.container:
            return False

        if not selection.get("Content"):
            return False

        return True

    @classmethod
    def execute(cls, character, selection=None):
        if not selection:
            return False

        container_object = selection.get("Container")
        container = container_object.container
        content = selection.get("Content")

        for game_object in content:
            if not container.add_item(game_object):
                continue
            target_level = game_object.location.level
            if target_level:
                target_level.remove_object(game_object)

        return True
