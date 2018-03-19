import inspect

from core.factories.character import CharacterFactory
from core.factories.items import ItemFactory
from core.factories.monster import MonsterFactory
from core.factories.treasure import TreasureFactory
from core.system import SystemObject


class Facade(SystemObject):
    def __init__(self, system):
        super().__init__(system)
        system.factory = self
        factories = (CharacterFactory, ItemFactory, MonsterFactory, TreasureFactory)
        self._factory_mapping = {}
        self._type_mapping = {}
        for factory in factories:
            factory_instance = factory(system)
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
                return factory.create_new(base_object_type)

        raise ValueError("No factory for base type {}".format(base_object_type))
