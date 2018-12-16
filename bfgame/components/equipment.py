from bfgame.components import Component
from bflib import units
from core import contexts
from core.messaging import StringBuilder, Actor, Target, Verb


class Equipment(Component):
    NAME = "equipment"
    __slots__ = ["armor_restrictions", "weapon_restrictions", "weapon_size_restrictions",
                 "wear_locations", "wield_locations", "empty_wield_locations"
                 "worn_items", "wielded_items"]
    """
    This component attaches itself to anything with a bodies.
    It represents equipment worn or wielded
    """
    def __init__(self):
        super().__init__()
        self.armor_restrictions = None
        self.weapon_restrictions = None
        self.weapon_size_restrictions = None

    def on_register(self, host):
        super().on_register(host)
        host_restrictions = self.host.restrictions
        if host_restrictions:
            self.armor_restrictions = host_restrictions.armor
            self.weapon_restrictions = host_restrictions.weapons
            self.weapon_size_restrictions = host_restrictions.weapon_size

    def copy(self):
        return Equipment()

    def remove(self, item):
        found_slots = False
        for item_slot in self.get_worn_item_slots():
            if item_slot.item == item:
                found_slots = True
                item_slot.item = None

        if found_slots:
            return True

        for item_slot in self.get_wielded_grasp_slots():
            if item_slot.item == item:
                item_slot.item = None
                found_slots = True

        if found_slots:
            return True

        return False

    def wear(self, item):
        if self.armor_restrictions and not self.armor_restrictions.can_wear(item.base):
            return False

        if not item.wearable:
            return False

        empty_item_slots = self.get_empty_item_slots()
        for wear_location_set in item.wearable.wear_locations:
            if hasattr(wear_location_set, '__iter__'):
                # Multiple Location Slot
                for slot in wear_location_set:
                    proper_slot = next((item_slot for item_slot in empty_item_slots
                                        if item_slot.keyword == slot), None)
                    if proper_slot is not None:
                        proper_slot.item = item
                    else:
                        return False

                context = contexts.Action(self.host, item)
                message = StringBuilder(Actor, Verb("wear", Actor), Target, ".")
                self.host.game.echo.see(self.host, message, context)

                return True
            else:
                # Single Location Slot
                proper_slot = next((item_slot for item_slot in empty_item_slots
                                    if item_slot.keyword == wear_location_set), None)
                if proper_slot is not None:
                    proper_slot.item = item
                    context = contexts.Action(self.host, item)
                    message = StringBuilder(Actor, Verb("wear", Actor), Target, ".")
                    self.host.game.echo.see(self.host, message, context)
                    return True
        return False

    def wield(self, item):
        if self.weapon_restrictions and not self.weapon_restrictions.can_wield(item.base):
            return False

        hands = 1
        if self.weapon_size_restrictions:
            keyword = self.weapon_size_restrictions.can_wield(item.base)
            if not keyword:
                return False
            else:
                if keyword == self.weapon_size_restrictions.keywords.NeedsTwoHands:
                    hands = 2

        empty_grasp_slots = self.get_empty_grasp_slots()
        if len(empty_grasp_slots) >= hands:
            while hands > 0:
                item_slot = empty_grasp_slots.pop(0)
                item_slot.item = item
                hands -= 1

            context = contexts.Action(self.host, item)
            message = StringBuilder(Actor, Verb("wield", Actor), Target, ".")
            self.host.game.echo.see(self.host, message, context)

            return True
        return False

    def get_melee_total_armor_class(self):
        all_items = self.get_all_items()
        armor_ac = sum([item.armor.armor_class for item in all_items if item.armor])
        shield_ac = sum([item.shield.armor_class_melee for item in all_items if item.shield])

        return armor_ac + shield_ac

    def get_ranged_total_armor_class(self):
        all_items = self.get_all_items()
        armor_ac = sum([item.armor.armor_class for item in all_items if item.armor])
        shield_ac = sum([item.shield.armor_class_missile for item in all_items if item.shield])

        return armor_ac + shield_ac

    def get_all_items(self):
        items = self.get_worn_items()
        items.extend(self.get_wielded_items())

        return items

    def get_empty_item_slots(self):
        body_parts = self.host.body.get_body_parts()
        return [item_slot for body_part in body_parts for item_slot in body_part.item_slots if not item_slot.item]

    def get_empty_grasp_slots(self):
        body_parts = self.host.body.get_body_parts()
        return [item_slot for body_part in body_parts for item_slot in body_part.grasp_slots if not item_slot.item]

    def get_worn_items(self):
        return [item_slot.item for item_slot in self.get_worn_item_slots()]

    def get_worn_item_slots(self):
        body_parts = self.host.body.get_body_parts()
        return [item_slot for body_part in body_parts for item_slot in body_part.item_slots if item_slot.item]

    def get_wielded_items(self):
        return [item_slot.item for item_slot in self.get_wielded_grasp_slots()]

    def get_wielded_grasp_slots(self):
        body_parts = self.host.body.get_body_parts()
        return [grasp_slot for body_part in body_parts for grasp_slot in body_part.grasp_slots if grasp_slot.item]

    def get_load_of_worn_items(self):
        worn_items = self.get_worn_items()
        total_weight = units.Pound(0)
        for item in worn_items:
            total_weight += item.weight.score

        return total_weight
