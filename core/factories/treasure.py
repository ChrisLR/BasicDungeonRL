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
    @singledispatch
    def generate(cls, treasure_type):
        return route_to_factory(treasure_type)

    @classmethod
    @generate.register(coins.Coin)
    def generate_coins(cls, treasure_type):
        return [route_to_factory(treasure_type)
                for _ in treasure_type.amount]

    @classmethod
    @generate.register(Jewelry)
    def generate_jewelry(cls, treasure_type):
        pass

    @classmethod
    @generate.register(Gem)
    def generate_gem(cls, treasure_type):
        pass

    @classmethod
    @generate.register(Potion)
    def generate_potion(cls, treasure_type):
        pass

    @classmethod
    @generate.register(MagicScroll)
    def generate_scroll(cls, treasure_type):
        pass

    @classmethod
    @generate.register(RandomMagicItem)
    def generate_magic_item(cls, treasure_type):
        pass

    @classmethod
    @generate.register(Weapon)
    def generate_magic_weapon(cls, treasure_type):
        pass

    @classmethod
    @generate.register(Armor)
    def generate_magic_armor(cls, treasure_type):
        pass

    def create_containers(self):
        pass
