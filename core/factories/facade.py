import inspect

from core.factories.character import CharacterFactory
from core.factories.items import ItemFactory
from core.factories.monster import MonsterFactory
from core.factories.treasure import TreasureFactory


class Facade(object):
    def __init__(self, game):
        self.game = game
        factories = (CharacterFactory, ItemFactory, MonsterFactory, TreasureFactory)
        self._factory_mapping = {}
        self._type_mapping = {}
        for factory in factories:
            factory_instance = factory(game)
            self._factory_mapping[factory.name] = factory_instance
            if factory.type_map is not None:
                self._type_mapping[factory.type_map] = factory_instance

    def get(self, factory_name):
        return self._factory_mapping.get(factory_name)

    def route(self, base_object_type):
        if not inspect.isclass(base_object_type):
            base_object_type = type(base_object_type)

        for base_type, factory in self._type_mapping.items():
            if issubclass(base_object_type, base_type):
                new_object = factory.create_new(base_object_type)
                new_object.game = self.game
                return new_object

        raise ValueError("No factory for base type {}".format(base_object_type))

    def create_new_character(self, ability_score_set, base_classes, base_race, name,
                             symbol, fg_color, bg_color, display_priority=0):
        new_object = self.get("character").create_new(
            ability_score_set, base_classes, base_race, name,
            symbol, fg_color, bg_color, display_priority
        )
        new_object.game = self.game

        return new_object
