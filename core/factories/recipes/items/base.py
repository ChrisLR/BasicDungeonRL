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

    @classmethod
    def build_components(cls):
        new_components = [
            components.Size(cls.base_item_type.size),
            components.Weight(cls.base_item_type.weight),
            components.Location(),
            components.Display(Colors.GRAY, Colors.BLACK, cls.base_item_type.name[0], DisplayPriority.Item),
        ]

        if cls.base_item_type.price:
            new_components.append(components.Sellable(cls.base_item_type.price))

        if cls.base_item_type.wear_locations:
            new_components.append(components.Wearable(cls.base_item_type.wear_locations))

        return new_components
