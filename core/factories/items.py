from bflib.items.base import Item
from core import flags
from core.factories.recipes import listing
from core.gameobject import GameObject


class ItemFactory(object):
    name = "item"
    type_map = Item

    def __init__(self, game):
        self.game = game

    def create_new(self, base_item):
        recipe = listing.get_recipe(base_item)
        if recipe is None:
            raise Exception("Found no recipes for item {}".format(base_item))

        item_components = self.get_recursive_components(base_item, recipe)
        new = GameObject(
            game=self.game,
            base=base_item,
            blocking=False,
            name=base_item.name
        )
        new.flags.add(flags.GameObjectFlags.Character)
        for component in item_components:
            new.register_component(component)

        return new

    def get_recursive_components(self, base_item, recipe, result_components=None):
        if result_components is None:
            result_components = []

        result_components.extend(recipe.build_components(base_item, self.game))
        for required_recipe in recipe.depends_on:
            self.get_recursive_components(base_item, required_recipe, result_components)

        return result_components
