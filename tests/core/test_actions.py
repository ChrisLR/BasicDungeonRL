from bflib.items import Backpack
from bflib.keywords.items import WearLocation, WieldLocation
from core import actions, components
from core.factories.items import ItemFactory
from core.tiles import doors
from core.world.level import Level


def test_action_open_door(sample_player):
    door = doors.WoodenDoor()
    actions.Open.execute(sample_player, [door])
    assert not door.openable.closed


def test_action_close_door(sample_player):
    door = doors.WoodenDoor()
    door.openable.open()
    actions.Close.execute(sample_player, [door])
    assert door.openable.closed


def test_action_drop(sample_player, sample_weapon):
    backpack = ItemFactory.create_new(Backpack)
    bare_bones_equipment = components.Equipment(wear_locations=WearLocation, wield_locations=WieldLocation)
    bare_bones_equipment.wear(backpack)
    sample_player.unregister_component(sample_player.equipment)
    sample_player.register_component(bare_bones_equipment)
    level = Level(100, 100)
    level.add_object(sample_player)
    coordinates = sample_player.location.get_local_coords()
    sample_player.inventory.add(sample_weapon)
    actions.Drop.execute(sample_player, [sample_weapon])

    assert sample_weapon not in sample_player.inventory.get_all_items()
    assert sample_weapon in level.get_objects_by_coordinates(coordinates)
