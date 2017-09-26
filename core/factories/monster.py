from bflib.monsters import animals, insects, reptilians
from core.gameobject import GameObject
from core import components


class MonsterFactory(object):
    @classmethod
    def create_new(cls, monster_type):
        new = GameObject(blocking=True, name=monster_type.name)
        new.register_component(components.Monster(monster_type))
        new.register_component(components.Health(monster_type.largest_hit_dice))
        new.register_component(components.Combat())
        new.register_component(components.Morale())

        movement = movement.MovementSet(walk=units.FeetPerGameTurn(80), turning_distance=units.Feet(10))
        no_appearing = AppearingSet(dice_wild=dice.D10(3))
        save_as = Fighter.level_table.levels[hit_dice.amount].saving_throws_set
        xp = 25


