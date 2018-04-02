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

    def __init__(self, game):
        self.game = game

    def create_new(self, treasure_type, wearable_for_size=None):
        row = TreasureTable.get_row(treasure_type)
        treasures = []
        for element in row.elements:
            if random.randint(1, 100) <= element.percent:
                for _ in range(element.amount):
                    if isinstance(element.treasure_value_type, collections.Iterable):
                        treasure_type = random.choice(element.treasure_value_type)
                    else:
                        treasure_type = element.treasure_value_type

                    treasure = self.generate(treasure_type)
                    if isinstance(treasure, collections.Iterable):
                        treasures.extend(treasure)
                    else:
                        treasures.append(treasure)

        containers = self.create_containers(treasures, wearable_for_size)
        return containers

    def create_containers(self, treasures, wearable_for_size=None):
        potential_containers = [
            container for container in listing.get_items_by_type(Container)
            if wearable_for_size is None or (
                    container.wear_locations and container.size <= wearable_for_size
            )
        ]

        created_containers = []
        while treasures:
            container = random.choice(potential_containers)
            built_container = self.game.factory.route(container)
            created_containers.append(built_container)
            for treasure in treasures.copy():
                if built_container.container.add_item(treasure):
                    treasures.remove(treasure)

        return created_containers

    def generate(self, treasure_type):
        generator = self._mapping.get(treasure_type, self.game.factory.route)
        return generator(treasure_type)

    def generate_coins(self, treasure_type):
        return [self.game.factory.route(treasure_type)
                for _ in treasure_type.amount]

    def generate_jewelry(self, treasure_type):
        pass

    def generate_gem(self, treasure_type):
        pass

    def generate_potion(self, treasure_type):
        pass

    def generate_scroll(self, treasure_type):
        pass

    def generate_magic_item(self, treasure_type):
        pass

    def generate_magic_weapon(self, treasure_type):
        pass

    def generate_magic_armor(self, treasure_type):
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
