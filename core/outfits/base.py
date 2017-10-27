from core.factories.items import ItemFactory


class Outfit(object):
    name = ""
    worn_items = []
    wielded_items = []
    inventory_items = []
    coins = None

    @classmethod
    def check_if_applicable(cls, game_object):
        return False

    @classmethod
    def apply(cls, game_object):
        if game_object.equipment:
            unpacked_worn_items = cls.unpack(cls.worn_items)
            unpacked_wielded_items = cls.unpack(cls.wielded_items)
            cls._equip_worn_items(unpacked_worn_items, game_object)
            cls._equip_wielded_items(unpacked_wielded_items, game_object)

        if game_object.inventory:
            unpacked_inventory_items = cls.unpack(cls.inventory_items)
            cls._add_inventory_items(unpacked_inventory_items, game_object)

    @staticmethod
    def _equip_worn_items(unpacked_worn_items, game_object):
        for item in unpacked_worn_items:
            built_item = ItemFactory.create_new(item)
            game_object.equipment.wear(built_item)

    @staticmethod
    def _equip_wielded_items(unpacked_wielded_items, game_object):
        for item in unpacked_wielded_items:
            built_item = ItemFactory.create_new(item)
            game_object.equipment.wield(built_item)

    @staticmethod
    def _add_inventory_items(unpacked_inventory_items, game_object):
        for item in unpacked_inventory_items:
            built_item = ItemFactory.create_new(item)
            game_object.inventory.add(built_item)

    @staticmethod
    def unpack(listing):
        unpacked_items = []
        for _ in range(0, len(listing)):
            item = listing.pop(-1)
            if isinstance(item, tuple):
                amount, item = item
                for _ in range(0, amount):
                    unpacked_items.append(item)
            else:
                unpacked_items.append(item)

        return unpacked_items
