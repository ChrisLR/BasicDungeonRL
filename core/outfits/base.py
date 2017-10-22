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
    def apply(cls):
        unpacked_worn_items = cls.unpack(cls.worn_items)
        unpacked_wielded_items = cls.unpack(cls.wielded_items)
        unpacked_inventory_items = cls.unpack(cls.inventory_items)


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

