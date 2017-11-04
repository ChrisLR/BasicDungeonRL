from bflib.items.base import Item
from core.factories.items import ItemFactory
from core import components


def Corpsify(game_object):
    new_corpse = ItemFactory.create_new(Item)
    new_corpse.register_component(components.Corpse(game_object))