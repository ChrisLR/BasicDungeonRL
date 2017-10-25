from bflib.items.lights.base import LightItem
from core import components
from core.factories.recipes import listing
from core.factories.recipes.base import Recipe
from core.factories.recipes.items.base import ItemRecipe


# noinspection PyTypeChecker
@listing.register
class LightRecipe(Recipe):
    name = "Base Light Recipe"
    base_item_type = LightItem
    depends_on = [ItemRecipe]

    @classmethod
    def build_components(cls):
        new_components = [
            components.Light(
                bright_light_radius=cls.base_item_type.bright_light_radius,
                dim_light_radius=cls.base_item_type.dim_light_radius,
                fuel=cls.base_item_type.fuel,
                fuel_duration=cls.base_item_type.fuel_duration,
                last_life_dice=cls.base_item_type.last_life_dice,
                light_shape=cls.base_item_type.light_shape,
            )
        ]

        return new_components
