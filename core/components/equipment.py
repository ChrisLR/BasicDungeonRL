from bflib import units
from core.components import Component


class Equipment(Component):
    NAME = "equipment"
    __slots__ = ["armor_restrictions", "weapon_restrictions", "weapon_size_restrictions",
                 "wear_locations", "wield_locations", "empty_wield_locations"
                 "worn_items", "wielded_items"]
    """
    This component attaches itself to anything with a bodies.
    It represents equipment worn or wielded
    """
    def __init__(self, wear_locations, wield_locations, armor_restrictions=None, weapon_restrictions=None,
                 weapon_size_restrictions=None):
        super().__init__()
        self.armor_restrictions = armor_restrictions
        self.weapon_restrictions = weapon_restrictions
        self.weapon_size_restrictions = weapon_size_restrictions

        self.wear_locations = wear_locations
        self.wield_locations = wield_locations
        self.empty_wield_locations = list(wear_locations)

        self.worn_items = {}
        self.wielded_items = {}

    def copy(self):
        new_equipment = Equipment(
            wear_locations=self.wear_locations,
            wield_locations=self.wield_locations,
            armor_restrictions=self.armor_restrictions,
            weapon_restrictions=self.weapon_restrictions
        )
        new_equipment.worn_items = {location: item.copy() for location, item in self.worn_items.items()}
        new_equipment.wielded_items = {location: item.copy() for location, item in self.wielded_items.items()}

        return new_equipment

    def remove_item(self, item):
        found_location = None
        for location, worn_item in self.worn_items.items():
            if worn_item == item:
                found_location = location
                break
        if found_location:
            self.empty_wield_locations.append(found_location)
            del self.worn_items[found_location]
            return True

        for location, wielded_item in self.wielded_items.items():
            if wielded_item == item:
                found_location = location
                break

        if found_location:
            self.empty_wield_locations.append(found_location)
            del self.wielded_items[found_location]
            return True

        return False

    def wear(self, item):
        if self.armor_restrictions and not self.armor_restrictions.can_wear(item):
            return False

        if not item.wearable:
            return False

        for wear_location_set in item.wearable.wear_locations:
            if hasattr(wear_location_set, '__iter__'):
                # Multiple Location Slot
                for slot in wear_location_set:
                    if self.worn_items.get(slot, None):
                        return False

                for slot in wear_location_set:
                    self.worn_items[slot] = item
            else:
                # Single Location Slot
                if not self.worn_items.get(wear_location_set, None):
                    self.worn_items[wear_location_set] = item
                    return True

        return False

    def wield(self, item):
        if self.weapon_restrictions and not self.weapon_restrictions.can_wield(item):
            return False

        hands = 1
        if self.weapon_size_restrictions:
            keyword = self.weapon_size_restrictions.can_wield(item)
            if not keyword:
                return False
            else:
                if keyword == self.weapon_size_restrictions.keywords.NeedsTwoHands:
                    hands = 2

        if len(self.empty_wield_locations) >= hands:
            while hands > 1:
                location = self.empty_wield_locations.pop(0)
                self.wielded_items[location] = item
                hands -= 1

            return True
        return False

    def get_total_armor_class(self):
        # TODO Once items are implemented, this should query all worn items for AC.
        return 0

    def get_all_items(self):
        items = list(self.worn_items.values())
        items.extend(self.wielded_items.values())
        return items

    def get_worn_items(self):
        return self.worn_items.values()

    def get_load_of_worn_items(self):
        worn_items = self.get_worn_items()
        total_weight = units.Pound(0)
        for item in worn_items:
            total_weight += item.weight

        return total_weight

    def get_wielded_items(self):
        return self.wielded_items.values()
