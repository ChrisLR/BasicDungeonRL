import collections
import random

from bflib.items import coins, listing
from bflib.items.armor.base import Armor
from bflib.items.containers.base import Container
from bflib.items.gems.base import Gem
from bflib.items.jewelry.base import Jewelry
from bflib.items.magical.scrolls.base import MagicScroll
from bflib.items.potions.base import Potion
from bflib.items.weapons.base import Weapon
from bflib.tables.treasure import TreasureTable, RandomMagicItem


class TreasureFactory(object):
    name = "treasure"
    type_map = None

    @classmethod
    def create_new(cls, treasure_type, wearable_for_size=None):
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

        containers = cls.create_containers(treasures, wearable_for_size)
        return containers

    @classmethod
    def create_containers(cls, treasures, wearable_for_size=None):
        potential_containers = [
            container for container in listing.get_items_by_type(Container)
            if wearable_for_size is None or (
                    container.wear_locations and container.size <= wearable_for_size
            )
        ]

        created_containers = []
        while treasures:
            container = random.choice(potential_containers)
            built_container = route_to_factory(container)
            created_containers.append(built_container)
            for treasure in treasures.copy():
                if built_container.container.add_item(treasure):
                    treasures.remove(treasure)

        return created_containers

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
        Potion: generate_potion,
        MagicScroll: generate_scroll,
        RandomMagicItem: generate_magic_item,
        Weapon: generate_magic_weapon,
    }
