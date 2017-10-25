from bflib.items.containers.base import Container, LiquidContainer, SpecialContainer
from core import components
from core.factories.recipes import listing
from core.factories.recipes.base import Recipe
from core.factories.recipes.items.base import ItemRecipe


# noinspection PyTypeChecker
@listing.register
class ContainerRecipe(Recipe):
    name = "Base Container Recipe"
    base_item_type = Container
    depends_on = [ItemRecipe]

    @classmethod
    def build_components(cls):
        new_components = [
            components.Container(
                container_type=cls.base_item_type.container_type,
                volume_limit=cls.base_item_type.volume_limit,
                weight_limit=cls.base_item_type.weight_limit
            )
        ]

        return new_components


# noinspection PyTypeChecker
@listing.register
class LiquidContainerRecipe(Recipe):
    name = "Base Liquid Container Recipe"
    base_item_type = LiquidContainer
    depends_on = [ItemRecipe]

    @classmethod
    def build_components(cls):
        new_components = [
            components.LiquidContainer(
                container_type=cls.base_item_type.container_type,
                volume_limit=cls.base_item_type.volume_limit
            )
        ]

        return new_components


# noinspection PyTypeChecker
@listing.register
class SpecialContainerRecipe(Recipe):
    name = "Base Special Container Recipe"
    base_item_type = SpecialContainer
    depends_on = [ItemRecipe]

    @classmethod
    def build_components(cls):
        new_components = [
            components.SpecialContainer(
                container_type=cls.base_item_type.container_type,
                containable_items=cls.base_item_type.containable_items,
                max_quantity=cls.base_item_type.max_quantity,
            )
        ]

        return new_components
