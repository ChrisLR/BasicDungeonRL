from bflib.items.base import Item
from bfgame import components
from bfgame.util.colors import Colors


def turn_into_corpse(game_object):
    # TODO This is lame
    item_factory = game_object.game.factory.get("item")
    new_corpse = item_factory.create_new(Item)
    new_corpse.name = "Corpse of " + game_object.name
    new_corpse.register_component(components.Corpse(game_object))
    new_corpse.display.ascii_character = '%'
    new_corpse.display.foreground_color = Colors.DARK_RED
    new_corpse.register_component(game_object.location.copy())
    level = game_object.location.level

    if game_object.weight:
        new_corpse.register_component(game_object.weight.copy())

    if game_object.equipment:
        wielded_weapons = list(game_object.equipment.get_wielded_items())
        for wielded_weapon in wielded_weapons:
            game_object.equipment.remove(wielded_weapon)
            wielded_weapon.location.set_local_coords(game_object.location.get_local_coords())
            level.add_object(wielded_weapon)

    if game_object.inventory:
        new_corpse.register_forward(game_object.inventory)

    level.remove_object(game_object)
    level.add_object(new_corpse)

    return new_corpse
