from core.actions.base import Action
from core.util import distance
from services.selection import CursorSelection, filters
from services.selection.base import TargetSelectionSet


class Fire(Action):
    name = "fire"
    target_selection = TargetSelectionSet(selections=CursorSelection, filters=filters.TileExclusion)

    def __init__(self, game):
        super().__init__(game)
        self.ranged_items = None
        self.target = None
        self.in_range_items = None
        self.ranged_items_with_ammo = None
        self.target_range = None

    def _is_ranged(self, target):
        return target.ranged

    def _has_health(self, target):
        return target.health

    def _in_range(self, item, target_range):
        return target_range <= item.ranged.range_set.long.value

    def _is_ammunition(self, item):
        if item.ammunition:
            return True

    def _get_ranged_items(self, character):
        if self.ranged_items is None:
            wielded_items = character.equipment.get_wielded_items()
            self.ranged_items = [item for item in wielded_items
                                 if self._is_ranged(item)]

        return self.ranged_items

    def _filter_out_ranged_items_without_ammo(self, character, ranged_items):
        if self.ranged_items_with_ammo is None:
            ammunition = {
                item: {item.base, item.ammunition.ammunition_type}
                for item in character.inventory.get_all_items()
                if self._is_ammunition(item)
            }

            ranged_items_with_ammo = set()
            compatible_ammo = {}
            for ranged_item in ranged_items:
                for ammo_item, ammunition_types in ammunition.items():
                    if ranged_item.ranged.ammunition_type in ammunition_types:
                        compatible_ammo[ammo_item] = ammunition_types
                        ranged_items_with_ammo.add(ranged_item)

            self.ranged_items_with_ammo = ranged_items_with_ammo
            self.compatible_ammo = compatible_ammo

        return self.ranged_items_with_ammo

    def _get_target(self, target_selection):
        # TODO A ray should be traced to see if another object is in the way.
        # TODO We should pass those objects to the ranged attack.
        if self.target is None:
            self.target = next(filter(self._has_health, target_selection), None)

        return self.target

    def _get_in_range_items(self, character, target, ranged_items):
        if self.in_range_items is None:
            character_coords = character.location.get_local_coords()
            target_coords = target.location.get_local_coords()
            self.target_range = distance.manhattan_distance_to(character_coords, target_coords)
            self.in_range_items = [
                ranged_item for ranged_item in ranged_items
                if self._in_range(ranged_item, self.target_range)
            ]

        return self.in_range_items

    def can_select(self, character):
        ranged_items = self._get_ranged_items(character)
        if not ranged_items:
            character.game.echo.player(character, "You are not wielding any ranged weapons.")
            return False

        ranged_items_with_ammo = self._filter_out_ranged_items_without_ammo(character, ranged_items)
        if not ranged_items_with_ammo:
            character.game.echo.player(character, "You have no ammunition for your ranged weapons.")
            return False

        return True

    def can_execute(self, character, target_selection=None):
        target = self._get_target(target_selection)
        if not target:
            return False

        in_range_items = self._get_in_range_items(character, target, self.ranged_items_with_ammo)
        if not in_range_items:
            character.game.echo.player(character, "Target is too far.")
            return False

        return True

    def execute(self, character, target_selection=None):
        ranged_items = self._get_ranged_items(character)
        ranged_items_with_ammo = self._filter_out_ranged_items_without_ammo(character, ranged_items)
        target = self._get_target(target_selection)
        in_range_items = self._get_in_range_items(character, target, ranged_items_with_ammo)
        ranged_attack = self.game.attacks.get_attack_by_name("ranged")
        ranged_attack.execute(
            attacker=character,
            defender=target,
            fired_weapons=in_range_items,
            distance=self.target_range,
            compatible_ammo=self.compatible_ammo
        )

        return True
