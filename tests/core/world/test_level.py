import random

import pytest

from bfgame import components
from bfgame.displaypriority import DisplayPriority
from core.gameobject import GameObject
from bfgame.tiles.base import Tile
from bfgame.util.colors import Colors
from core.world import Level


@pytest.fixture
def game_objects():
    # noinspection PyShadowingNames
    game_objects = []
    for i in range(0, 10):
        game_object = GameObject(blocking=bool(random.randint(0, 1)), name=str(i))
        game_object.register_component(components.Location())
        game_object.location.set_local_coords((random.randint(0, 100), random.randint(0, 100)))
        game_objects.append(game_object)

    return game_objects


# noinspection PyShadowingNames
def test_game_objects_property(game_objects):
    level = Level(100, 100)
    for game_object in game_objects:
        level.add_object(game_object)

    level_objects = level.game_objects

    assert level_objects
    for game_object in game_objects:
        assert game_object in level_objects


def test_add_object_with_display():
    level = Level(100, 100)
    game_object = GameObject(name="Displayable")
    game_object.register_component(components.Display(
        Colors.DARK_RED, Colors.BLACK, '!', priority=DisplayPriority.Item)
    )
    level.add_object(game_object)

    assert game_object in level.displays[DisplayPriority.Item]
    for key, display_objects in level.displays.items():
        if key != DisplayPriority.Item:
            assert game_object not in display_objects


def test_add_object_with_location():
    level = Level(100, 100)
    coordinates = (10, 10)
    game_object = GameObject(name="Loc")
    game_object.register_component(components.Location())
    game_object.location.set_local_coords(coordinates)
    level.add_object(game_object)

    assert game_object in level.get_objects_by_coordinates(coordinates)


def test_remove_object_with_display():
    level = Level(100, 100)
    game_object = GameObject(name="Displayable")
    game_object.register_component(components.Display(
        Colors.DARK_RED, Colors.BLACK, '!', priority=DisplayPriority.Item)
    )
    level.add_object(game_object)
    level.remove_object(game_object)

    for key, display_objects in level.displays.items():
        assert game_object not in display_objects


def test_remove_object_with_location():
    level = Level(100, 100)
    coordinates = (10, 10)
    game_object = GameObject(name="Loc")
    game_object.register_component(components.Location())
    game_object.location.set_local_coords(coordinates)
    level.add_object(game_object)
    level.remove_object(game_object)

    assert game_object not in level.get_objects_by_coordinates(coordinates)


def test_add_tile():
    level = Level(100, 100)
    coordinates = (10, 10)
    tile = Tile
    level.add_tile(coordinates, tile)

    assert isinstance(level.tiles[coordinates], tile)


def test_get_tile():
    level = Level(100, 100)
    coordinates = (10, 10)
    tile = Tile
    level.add_tile(coordinates, tile)

    assert isinstance(level.get_tile(coordinates), tile)


def test_remove_tile():
    level = Level(100, 100)
    coordinates = (10, 10)
    tile = Tile
    level.add_tile(coordinates, tile)
    level.remove_tile(coordinates)

    assert level.get_tile(coordinates) is None


def test_adjust_coordinates_for_object():
    level = Level(100, 100)
    coordinates = (10, 10)
    new_coordinates = (50, 50)
    game_object = GameObject(name="Loc")
    game_object.register_component(components.Location())
    game_object.location.set_local_coords(coordinates)
    level.add_object(game_object)
    level.adjust_coordinates_for_object(game_object, new_coordinates)

    assert game_object not in level.get_objects_by_coordinates(coordinates)
    assert game_object in level.get_objects_by_coordinates(new_coordinates)
