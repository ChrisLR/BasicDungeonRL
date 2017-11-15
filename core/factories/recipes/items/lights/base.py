from bflib.items.lights.base import LightItem
from core import components
from core.factories.recipes import listing
from core.factories.recipes.base import Recipe
from core.factories.recipes.items.base import ItemRecipe


# noinspection PyTypeChecker
@listing.register
class LightRecipe(Recipe):
    name = "Base Light Recipe"
    base_object_type = LightItem
    depends_on = [ItemRecipe]

    @staticmethod
    def build_components(item_type):
        new_components = [
            components.Light(
                bright_light_radius=item_type.bright_light_radius,
                dim_light_radius=item_type.dim_light_radius,
                fuel=item_type.fuel,
                fuel_duration=item_type.fuel_duration,
                last_life_dice=item_type.last_life_dice,
                light_shape=item_type.light_shape,
            )
        ]

        return new_components
