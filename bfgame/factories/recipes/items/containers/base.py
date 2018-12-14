from bflib.items.containers.base import Container, LiquidContainer, SpecialContainer
from bfgame import components
from bfgame.factories.recipes import listing
from bfgame.factories.recipes.base import Recipe
from bfgame.factories.recipes.items.base import ItemRecipe


# noinspection PyTypeChecker
@listing.register
class ContainerRecipe(Recipe):
    name = "Base Container Recipe"
    base_object_type = Container
    depends_on = [ItemRecipe]

    @staticmethod
    def build_components(item_type, game):
        new_components = [
            components.Container(
                container_type=item_type.container_type,
                volume_limit=item_type.volume_limit,
                weight_limit=item_type.weight_limit
            )
        ]

        return new_components


# noinspection PyTypeChecker
@listing.register
class LiquidContainerRecipe(Recipe):
    name = "Base Liquid Container Recipe"
    base_object_type = LiquidContainer
    depends_on = [ItemRecipe]

    @staticmethod
    def build_components(item_type, game):
        new_components = [
            components.LiquidContainer(
                container_type=item_type.container_type,
                volume_limit=item_type.volume_limit
            )
        ]

        return new_components


# noinspection PyTypeChecker
@listing.register
class SpecialContainerRecipe(Recipe):
    name = "Base Special Container Recipe"
    base_object_type = SpecialContainer
    depends_on = [ItemRecipe]

    @staticmethod
    def build_components(item_type, game):
        new_components = [
            components.SpecialContainer(
                container_type=item_type.container_type,
                containable_items=item_type.containable_items,
                max_quantity=item_type.max_quantity,
            )
        ]

        return new_components
