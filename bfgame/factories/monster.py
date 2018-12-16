import random

from bflib.monsters.base import Monster
from bfgame import components
from core import flags
from bfgame.factories.recipes import listing
from bfgame.factories.treasure import TreasureFactory
from core.gameobject import GameObject


class MonsterFactory(object):
    name = "monster"
    type_map = Monster

    def __init__(self, game):
        self.game = game

    def create_new(self, base_monster):
        recipe = listing.get_recipe(base_monster)
        if recipe is None:
            raise Exception("Found no recipes for monster {}".format(base_monster))

        item_components = self.get_recursive_components(base_monster, recipe)
        new = GameObject(
            game=self.game,
            base=base_monster,
            blocking=True,
            name=base_monster.name
        )
        new.flags.add(flags.GameObjectFlags.Character)
        for component in item_components:
            new.register_component(component)

        if new.equipment:
            new.register_component(components.Inventory())

            if base_monster.treasure_type:
                items = TreasureFactory.create_new(base_monster.treasure_type)
                for item in items:
                    if not item.wearable or not new.equipment.wear(item):
                        new.inventory.add(item)

        if recipe.outfits:
            outfit = random.choice(recipe.outfits)
            outfit.apply(self.game, new)

        if not new.vision:
            new.register_component(components.SimpleVision())

        new.register_component(components.Effects())
        new.register_component(components.Alliance())

        return new

    def get_recursive_components(self, base_monster, recipe, result_components=None):
        if result_components is None:
            result_components = []

        built_components = recipe.build_components(base_monster, self.game)
        if built_components:
            result_components.extend(built_components)

        for required_recipe in recipe.depends_on:
            self.get_recursive_components(base_monster, required_recipe, result_components)

        return result_components
