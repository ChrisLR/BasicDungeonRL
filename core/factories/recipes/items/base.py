from bflib.items.base import Item
from core.factories.recipes.base import Recipe
from core import components
from core.util.colors import Colors
from core.displaypriority import DisplayPriority


class ItemRecipe(Recipe):
    name = "Base Item Recipe"
    base_item_type = Item
    depends_on = []

    @classmethod
    def build_components(cls):
        return [
            components.Sellable(cls.base_item_type.price),
            components.Size(cls.base_item_type.size),
            components.Wearable(cls.base_item_type.wear_locations),
            components.Weight(cls.base_item_type.weight),
            components.Location(),
            components.Display(Colors.GRAY, Colors.BLACK, cls.base_item_type.name[0], DisplayPriority.Item),
        ]
