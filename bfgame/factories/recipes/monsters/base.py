from bfgame import components as bf_components
from bfgame.factories.recipes import listing, Recipe
from bflib.monsters.base import Monster
from core import components
from core.displaypriority import DisplayPriority
from core.util.colors import Colors


# noinspection PyTypeChecker
@listing.register
class MonsterRecipe(Recipe):
    name = "Base Monster Recipe"
    base_object_type = Monster
    depends_on = []
    outfits = None

    @staticmethod
    def build_components(monster_type, game):
        name = monster_type.name if monster_type.name else monster_type.__name__

        new_components = [
            components.Display(Colors.RED, Colors.BLACK, name[0], DisplayPriority.Enemy),
            components.Location(),
            bf_components.Monster(monster_type),
            components.Effects(),
            bf_components.Health(),
            bf_components.Combat(),
            components.Size(monster_type.size),
            bf_components.SavingThrows(monster_type.save_as),
            bf_components.SpawnInfo(monster_type.no_appearing),
            bf_components.Morale(monster_type.morale),
            bf_components.Money(),
            bf_components.Movement(monster_type.movement),
            components.Weight(monster_type.weight),
        ]

        return new_components
