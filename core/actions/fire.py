from core.actions.base import Action
from services.selection import CursorSelection, filters
from services.selection.base import TargetSelectionSet
from core.util import distance
from functools import partial


class Fire(Action):
    name = "fire"
    target_selection = TargetSelectionSet(selections=CursorSelection, filters=filters.TileExclusion)

    def _is_ranged(self, target):
        return target.ranged

    def _has_health(self, target):
        return target.health

    def _in_range(self, item, target_range):
        return target_range <= item.ranged.range_set.long.value

    def can_execute(self, character, target_selection=None):
        wielded_items = character.equipment.get_wielded_items()
        ranged_items = filter(self._is_ranged, wielded_items)
        if not ranged_items:
            character.game.echo.player(character, "You are not wielding any ranged weapons.")
            return False

        target = next(filter(self._has_health, target_selection), None)
        if not target:
            return False

        character_coords = character.location.get_local_coords()
        target_coords = target.location.get_local_coords()
        target_range = distance.manhattan_distance_to(character_coords, target_coords)
        in_range_items = filter(partial(self._in_range, target_range=target_range), ranged_items)
        if not in_range_items:
            character.game.echo.player(character, "Target is too far.")
            return False

        return True

    def execute(self, character, target_selection=None):
        wielded_items = character.equipment.get_wielded_items()
        ranged_items = filter(self._is_ranged, wielded_items)
        if not ranged_items:
            character.game.echo.player(character, "You are not wielding any ranged weapons.")
            return False

        target = next(filter(self._has_health, target_selection), None)
        if not target:
            return False

        character_coords = character.location.get_local_coords()
        target_coords = target.location.get_local_coords()
        target_range = distance.manhattan_distance_to(character_coords, target_coords)
        in_range_items = filter(partial(self._in_range, target_range=target_range), ranged_items)
        if not in_range_items:
            character.game.echo.player(character, "Target is too far.")
            return False

        return True
