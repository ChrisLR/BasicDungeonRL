from core.gameobject import GameObject
from core import components
from core.util.colors import Colors
from core.displaypriority import DisplayPriority


class MonsterFactory(object):
    @classmethod
    def create_new(cls, monster_type):
        new = GameObject(blocking=True, name=monster_type.name)
        new.register_component(components.Monster(monster_type))
        new.register_component(components.Health())
        new.register_component(components.Combat())
        new.register_component(components.Morale())
        new.register_component(components.Movement(monster_type.movement_set))
        new.register_component(components.SpawnInfo(monster_type.no_appearing))
        new.register_component(components.SavingThrows(monster_type.save_as))
        new.register_component(components.Money())
        new.register_component(components.Location())
        new.register_component(components.Display(Colors.RED, Colors.BLACK, "D", DisplayPriority.Enemy))
