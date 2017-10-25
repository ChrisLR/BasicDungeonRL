"""
The base idea behind recipes is that it tells the factory
what components to use to build the item.
It should use an inheritance system to avoid having thousands recipes for every item
but it should always take specific first and recurse subclasses
"""


class Recipe(object):
    name = ""
    base_item_type = None

    def build(self, game_object):
        pass
