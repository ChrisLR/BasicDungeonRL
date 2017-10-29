from core.factories.recipes import listing
from core.gameobject import GameObject


class ItemFactory(object):
    @classmethod
    def create_new(cls, base_item):
        try:
            recipe = listing.get_recipe(base_item)
            if recipe is None:
                raise Exception("Found no recipes for item {}".format(base_item))

            item_components = cls.get_recursive_components(base_item, recipe)
            new = GameObject(blocking=False, name=base_item.name)
            for component in item_components:
                new.register_component(component)
        except Exception as exception:
            raise

        return new

    @classmethod
    def get_recursive_components(cls, base_item, recipe, result_components=None):
        if result_components is None:
            result_components = []

        result_components.extend(recipe.build_components(base_item))
        for required_recipe in recipe.depends_on:
            cls.get_recursive_components(base_item, required_recipe, result_components)

        return result_components