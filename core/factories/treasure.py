from bflib.tables.treasure import TreasureTable, RandomMagicItem
from bflib import dice
from bflib.items import coins
from bflib.items.armor.base import Armor
from bflib.items.gems.base import Gem
from bflib.items.jewelry.base import Jewelry
from bflib.items.potions.base import Potion
from bflib.items.weapons.base import Weapon
from bflib.items.writing.magical import MagicScroll
from bflib.treasuretypes import TreasureType
from core.factories.router import route_to_factory
import collections
import random
from functools import singledispatch


class TreasureFactory(object):
    """
    This
    """

    @classmethod
    def create_new(cls, treasure_type):
        row = TreasureTable.get_row(treasure_type)
        treasures = []
        for element in row.elements:
            if random.randint(1, 100) <= element.percent:
                for _ in range(element.amount):
                    if isinstance(element.treasure_value_type, collections.Iterable):
                        treasure_type = random.choice(element.treasure_value_type)
                    else:
                        treasure_type = element.treasure_value_type

                    treasure = cls.generate(treasure_type)
                    if isinstance(treasure, collections.Iterable):
                        treasures.extend(treasure)
                    else:
                        treasures.append(treasure)

    @classmethod
    def create_containers(cls):
        pass

    @classmethod
    def generate(cls, treasure_type):
        generator = cls._mapping.get(treasure_type, route_to_factory)
        return generator(treasure_type)

    @classmethod
    def generate_coins(cls, treasure_type):
        return [route_to_factory(treasure_type)
                for _ in treasure_type.amount]

    @classmethod
    def generate_jewelry(cls, treasure_type):
        pass

    @classmethod
    def generate_gem(cls, treasure_type):
        pass

    @classmethod
    def generate_potion(cls, treasure_type):
        pass

    @classmethod
    def generate_scroll(cls, treasure_type):
        pass

    @classmethod
    def generate_magic_item(cls, treasure_type):
        pass

    @classmethod
    def generate_magic_weapon(cls, treasure_type):
        pass

    @classmethod
    def generate_magic_armor(cls, treasure_type):
        pass

    _mapping = {
        Armor: generate_magic_armor,
        coins.Coin: generate_coins,
        Jewelry: generate_jewelry,
        Gem: generate_gem,
        Potion:generate_potion,
        MagicScroll: generate_scroll,
        RandomMagicItem: generate_magic_item,
        Weapon: generate_magic_weapon,
    }

