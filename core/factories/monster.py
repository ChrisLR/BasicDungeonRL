import random

from core import components, flags
from core.factories.recipes import listing
from core.gameobject import GameObject


class MonsterFactory(object):
    @classmethod
    def create_new(cls, base_monster):
        recipe = listing.get_recipe(base_monster)
        if recipe is None:
            raise Exception("Found no recipes for monster {}".format(base_monster))

        item_components = cls.get_recursive_components(base_monster, recipe)
        new = GameObject(blocking=True, name=base_monster.name)
        new.flags.add(flags.GameObjectFlags.Character)
        for component in item_components:
            new.register_component(component)

        if recipe.outfits:
            outfit = random.choice(recipe.outfits)
            outfit.apply(new)

        if new.equipment:
            new.register_component(components.Inventory())

        if base_monster.treasure_type:
            # TODO Call Treasure Factory here.
            pass

        return new

    @classmethod
    def get_recursive_components(cls, base_monster, recipe, result_components=None):
        if result_components is None:
            result_components = []

        built_components = recipe.build_components(base_monster)
        if built_components:
            result_components.extend(built_components)

        for required_recipe in recipe.depends_on:
            cls.get_recursive_components(base_monster, required_recipe, result_components)

        return result_components
