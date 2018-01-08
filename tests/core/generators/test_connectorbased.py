from core.generators.base import ConnectorBasedGenerator
from core.generators.maps.base import MapPiece
from core.world.level import Level
import pytest


@pytest.fixture
def generator():
    return ConnectorBasedGenerator()


def test_generate(cls, level):
    # This be integration testing, ignored for now.
    pass


def test_prepare_spawn_grid_has_correct_size(generator):
    new_level = Level(10, 10)
    spawn_grid = generator._prepare_spawn_grid(new_level)

    assert len(spawn_grid) == 100


def test_prepare_spawn_grid_use_coordinates(generator):
    new_level = Level(10, 10)
    spawn_grid = generator._prepare_spawn_grid(new_level)

    for coordinate in spawn_grid:
        x, y = coordinate
        assert isinstance(coordinate, tuple)
        assert isinstance(x, int)
        assert isinstance(y, int)


def test_get_origin_from_piece_center(generator):
    class TestPiece(MapPiece):
        tiles = "###\n###\n###"

    center_coordinate = (50, 51)
    origin = generator._get_origin_from_piece_center(
        center_coordinate, TestPiece)

    x, y = origin
    assert x == 49
    assert y == 50


def test_get_center_coordinate(generator):
    level = Level(100, 100)
    x, y = generator._get_center_coordinate(level)

    assert x == 50
    assert y == 50


def test_get_pieces_by_connectors_amount(cls):
    pass


def test_write_piece(
        cls, level, piece, spawn_grid, pointer_coords,
        unresolved_connectors, origin_direction=None):
    pass

def test_add_unresolved_connectors(
        cls, piece, pointer_coords,
        unresolved_connectors, origin_direction=None):

    pass


def test_get_connector_coord(cls, connector, pointer_coord):
    pass


def _resolve_next_connectors(
        cls, level, spawn_grid, unresolved_connectors):
    pass


def test_fill_empty_spaces(cls, level, rejected_tiles):
    pass


def test_get_compatible_pieces(cls, origin_direction, connector):
    pass


def _all_tiles_fit(cls, piece, spawn_grid, origin_coord):
    pass


def test_get_origin_for_new_piece(cls, direction, piece, connector_coord):
    pass
