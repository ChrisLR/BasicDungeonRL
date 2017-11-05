from bflib.items.base import Item
from core import components
from core.factories.items import ItemFactory
from core.util.colors import Colors


def turn_into_corpse(game_object):
    new_corpse = ItemFactory.create_new(Item)
    new_corpse.register_component(components.Corpse(game_object))
    new_corpse.display.ascii_character = '%'
    new_corpse.display.foreground_color = Colors.DARK_RED
    new_corpse.register_component(game_object.location.copy())
    level = game_object.location.level
    level.remove_object(game_object)
    level.add_object(new_corpse)

    return new_corpse
