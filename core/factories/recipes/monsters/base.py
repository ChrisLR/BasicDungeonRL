from bflib.monsters.base import Monster
from core import components
from core.ai import personalities
from core.displaypriority import DisplayPriority
from core.factories.recipes import listing, Recipe
from core.util.colors import Colors


# noinspection PyTypeChecker
@listing.register
class MonsterRecipe(Recipe):
    name = "Base Monster Recipe"
    base_object_type = Monster
    depends_on = []
    outfits = None

    @staticmethod
    def build_components(monster_type):
        name = monster_type.name if monster_type.name else monster_type.__name__

        new_components = [
            components.Display(Colors.RED, Colors.BLACK, name[0], DisplayPriority.Enemy),
            components.Location(),
            components.Monster(monster_type),
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
