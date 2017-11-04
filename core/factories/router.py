from bflib.characters.base import Character
from bflib.items.base import Item
from bflib.monsters.base import Monster
from core.factories.character import CharacterFactory
from core.factories.items import ItemFactory
from core.factories.monster import MonsterFactory

type_mapping = {
    Item: ItemFactory,
    Character: CharacterFactory,
    Monster: MonsterFactory,
}
types = [Item, Character, Monster]


def route_to_factory(base_object_type):
    for base_type in types:
        if issubclass(base_object_type, base_type):
            factory = type_mapping.get(base_type, None)
            if factory is None:
                raise Exception("No factory for base type {}".format(base_type))
            return factory.create_new(base_object_type)
