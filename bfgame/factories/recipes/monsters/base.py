from bflib.monsters.base import Monster
from bfgame import components
from bfgame.ai import personalities
from bfgame.displaypriority import DisplayPriority
from bfgame.factories.recipes import listing, Recipe
from bfgame.util.colors import Colors


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
            components.Monster(monster_type),
            components.Effects(),
            components.Health(),
            components.Combat(),
            components.Size(monster_type.size),
            components.SavingThrows(monster_type.save_as),
            components.SpawnInfo(monster_type.no_appearing),
            components.Morale(monster_type.morale),
            components.Money(),
            components.Movement(monster_type.movement),
            components.Weight(monster_type.weight),
        ]

        return new_components
