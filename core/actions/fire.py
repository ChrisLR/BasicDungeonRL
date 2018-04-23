from core.actions.base import Action
from services.selection import CursorSelection, filters
from services.selection.base import TargetSelectionSet
from core.util import distance
from functools import partial


class Fire(Action):
    name = "fire"
    target_selection = TargetSelectionSet(selections=CursorSelection, filters=filters.TileExclusion)

    def __init__(self, game):
        super().__init__(game)
        self.ranged_items = None
        self.target = None
        self.in_range_items = None

    def _is_ranged(self, target):
        return target.ranged

    def _has_health(self, target):
        return target.health

    def _in_range(self, item, target_range):
        return target_range <= item.ranged.range_set.long.value

    def _get_ranged_items(self, character):
        if self.ranged_items is None:
            wielded_items = character.equipment.get_wielded_items()
            self.ranged_items = filter(self._is_ranged, wielded_items)

        return self.ranged_items

    def _get_target(self, target_selection):
        if self.target is None:
            self.target = next(filter(self._has_health, target_selection), None)

        return self.target

    def _get_in_range_items(self, character, target, ranged_items):
        if self.in_range_items is None:
            character_coords = character.location.get_local_coords()
            target_coords = target.location.get_local_coords()
            target_range = distance.manhattan_distance_to(character_coords, target_coords)
            self.in_range_items = filter(
                partial(self._in_range, target_range=target_range),
                ranged_items
            )

        return self.in_range_items

    def can_execute(self, character, target_selection=None):
        ranged_items = self._get_ranged_items(character)
        if not ranged_items:
            character.game.echo.player(character, "You are not wielding any ranged weapons.")
            return False

        # TODO Filter out weapons without ammo

        target = self._get_target(target_selection)
        if not target:
            return False

        in_range_items = self._get_in_range_items(character, target, ranged_items)
        if not in_range_items:
            character.game.echo.player(character, "Target is too far.")
            return False

        return True

    def execute(self, character, target_selection=None):
        ranged_items = self._get_ranged_items(character)
        target = self._get_target(target_selection)
        in_range_items = self._get_in_range_items(character, target, ranged_items)

        return True
