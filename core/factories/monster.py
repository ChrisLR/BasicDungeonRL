from core.factories.recipes import listing
from core.gameobject import GameObject


class MonsterFactory(object):
    @classmethod
    def create_new(cls, base_monster):
        try:
            recipe = listing.get_recipe(base_monster)
            if recipe is None:
                raise Exception("Found no recipes for monster {}".format(base_monster))

            item_components = cls.get_recursive_components(base_monster, recipe)
            new = GameObject(blocking=True, name=base_monster.name)
            for component in item_components:
                new.register_component(component)
        except Exception as exception:
            raise

        return new

    @classmethod
    def get_recursive_components(cls, base_monster, recipe, result_components=None):
        if result_components is None:
            result_components = []

        result_components.extend(recipe.build_components(base_monster))
        for required_recipe in recipe.depends_on:
            cls.get_recursive_components(base_monster, required_recipe, result_components)

        return result_components
