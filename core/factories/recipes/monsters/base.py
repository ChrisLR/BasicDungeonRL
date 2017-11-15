from bflib.monsters.base import Monster
from core import components
from core.displaypriority import DisplayPriority
from core.factories.recipes import listing
from core.factories.recipes.base import Recipe
from core.util.colors import Colors


# noinspection PyTypeChecker
@listing.register
class MonsterRecipe(Recipe):
    name = "Base Monster Recipe"
    base_object_type = Monster
    depends_on = []

    @staticmethod
    def build_components(monster_type):
        name = monster_type.name if monster_type.name else monster_type.__name__

        # TODO This is the basic attributes of a monster.
        # TODO We need to find a way to translate this to core game terms.
        # attack_bonus = 0
        # attack_sets = []
        # base_armor_class = 0
        # carry_capacity = CarryCapacity
        # hit_dice = dice.Dice
        # morale = 0
        # movement = movement.MovementSet
        # no_appearing = AppearingSet
        # save_as = Fighter.level_table.levels[1].saving_throws_set
        # special_abilities = specialabilities.SpecialAbilitySet
        # treasure_type = TreasureType
        # xp = 0


        # new_components = [
        #     components.Size(item_type.size),
        #     components.Weight(item_type.weight),
        #     components.Location(),
        #     components.Display(Colors.GRAY, Colors.BLACK, name[0], DisplayPriority.Item),
        # ]
        #
        # if item_type.price:
        #     new_components.append(components.Sellable(item_type.price))
        #
        # if item_type.wear_locations:
        #     new_components.append(components.Wearable(item_type.wear_locations))

        return new_components
