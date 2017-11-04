from bflib.items.base import Item
from core import components
from core.displaypriority import DisplayPriority
from core.factories.recipes import listing
from core.factories.recipes.base import Recipe
from core.util.colors import Colors


# noinspection PyTypeChecker
@listing.register
class ItemRecipe(Recipe):
    name = "Base Item Recipe"
    base_item_type = Item
    depends_on = []

    @staticmethod
    def build_components(item_type):
        name = item_type.name if item_type.name else item_type.__name__

        new_components = [
            components.Size(item_type.size),
            components.Weight(item_type.weight),
            components.Location(),
            components.Display(Colors.GRAY, Colors.BLACK, name[0], DisplayPriority.Item),
        ]

        if item_type.price:
            new_components.append(components.Sellable(item_type.price))

        if item_type.wear_locations:
            new_components.append(components.Wearable(item_type.wear_locations))

        return new_components
