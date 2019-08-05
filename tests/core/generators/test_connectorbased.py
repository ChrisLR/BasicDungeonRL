from bflib.monsters import Deer
from core.generators.base import ConnectorBasedGenerator
from core.maps.base import MapPiece, Connector, ConnectorLink
from bfgame.generators.spawns import OnceSpawner, SpawnSet
from core.direction import Direction
from core.world import Level
from bfgame.tiles import floors
import pytest


@pytest.fixture
def generator():
    return ConnectorBasedGenerator()


class TestPieceOne(MapPiece):
    tiles = "###\n###\n###"
    symbolic_links = {"#": floors.DungeonFloor}
    connectors = {
        Direction.North: (Connector((1, 0)),)
    }


class TestPieceTwo(MapPiece):
    tiles = "###\n###\n###"
    symbolic_links = {"#": floors.DungeonFloor}
    connectors = {
        Direction.North: (Connector((1, 0)),),
        Direction.South: (Connector((1, 2)),),
    }


class TestPieceThree(MapPiece):
    tiles = "###\n###\n###"
    symbolic_links = {"#": floors.DungeonFloor}
    connectors = {
        Direction.West: (Connector((0, 1)),),
        Direction.East: (Connector((2, 1)),),
    }


class TestPieceFour(MapPiece):
    tiles = "###\n###\n###"
    symbolic_links = {"#": floors.DungeonFloor}
    connectors = {
        Direction.North: (Connector((1, 0)),),
        Direction.East: (Connector((1, 1)),),
        Direction.South: (Connector((1, 2)),),
        Direction.West: (Connector((0, 1)),),
    }


class TestPieceOneWithSpawner(MapPiece):
    tiles = "###\n###\n###"
    symbolic_links = {"#": floors.DungeonFloor}
    connectors = {Direction.North: (Connector((1, 0)),)}
    spawners = [OnceSpawner(SpawnSet(100, Deer, (1, 1)))]


def test_generate():
    # This be integration testing, ignored for now.
    pass


# noinspection PyShadowingNames
def test_prepare_spawn_grid_has_correct_size(generator):
    new_level = Level(10, 10)
    spawn_grid = generator._prepare_spawn_grid(new_level)

    assert len(spawn_grid) == 100


# noinspection PyShadowingNames
def test_prepare_spawn_grid_use_coordinates(generator):
    new_level = Level(10, 10)
    spawn_grid = generator._prepare_spawn_grid(new_level)

    for coordinate in spawn_grid:
        x, y = coordinate
        assert isinstance(coordinate, tuple)
        assert isinstance(x, int)
        assert isinstance(y, int)


# noinspection PyShadowingNames
def test_get_origin_from_piece_center(generator):
    center_coordinate = (50, 51)
    origin = generator._get_origin_from_piece_center(
        center_coordinate, TestPieceOne)

    x, y = origin
    assert x == 49
    assert y == 50


# noinspection PyShadowingNames
def test_get_center_coordinate(generator):
    level = Level(100, 100)
    x, y = generator._get_center_coordinate(level)

    assert x == 50
    assert y == 50


def test_get_pieces_by_connectors_amount():
    class TestGenerator(ConnectorBasedGenerator):
        pieces = [
            (100, TestPieceOne),
            (100, TestPieceTwo)
        ]

    pieces = TestGenerator._get_pieces_by_connectors_amount()

    assert pieces[0] is TestPieceTwo
    assert pieces[1] is TestPieceOne


# noinspection PyShadowingNames
def test_write_piece_with_no_origin(generator):
    level = Level(50, 50)
    spawn_grid = generator._prepare_spawn_grid(level)
    pointer_coordinate = (10, 20)
    unresolved_connectors = []

    generator._write_piece(
        level,
        TestPieceOneWithSpawner,
        spawn_grid,
        pointer_coordinate,
        unresolved_connectors
    )

    assert len(level.rooms) == 1
    assert level.rooms[0].design_piece is TestPieceOneWithSpawner
    assert len(unresolved_connectors) == 1
    assert len(spawn_grid) == 2491
    assert len(level.game_objects) == 1


def test_add_unresolved_connectors_with_one_connector(generator):
    unresolved_connectors = []
    pointer_coordinate = (1, 1)

    generator._add_unresolved_connectors(
        TestPieceOne,
        pointer_coordinate,
        unresolved_connectors,
    )

    assert len(unresolved_connectors) == 1
    assert isinstance(unresolved_connectors[0], ConnectorLink)
    assert isinstance(unresolved_connectors[0].connector, Connector)
    assert unresolved_connectors[0].coordinate == (2, 1)
    assert unresolved_connectors[0].direction == Direction.North


def test_add_unresolved_connectors_with_four_connectors(generator):
    unresolved_connectors = []
    pointer_coordinate = (0, 0)

    generator._add_unresolved_connectors(
        TestPieceFour,
        pointer_coordinate,
        unresolved_connectors,
    )

    assert len(unresolved_connectors) == 4
    for direction, connector in TestPieceFour.connectors.items():
        connector_link = next((link for link in unresolved_connectors
                               if link.direction is direction))
        assert isinstance(connector_link, ConnectorLink)
        assert isinstance(connector_link.connector, Connector)
        assert connector_link.coordinate == connector[0].local_coordinates[0]


def test_add_unresolved_connectors_with_origin(generator):
    unresolved_connectors = []
    pointer_coordinate = (1, 1)

    generator._add_unresolved_connectors(
        TestPieceTwo,
        pointer_coordinate,
        unresolved_connectors,
        origin_direction=Direction.South
    )

    assert len(unresolved_connectors) == 1
    assert unresolved_connectors[0].coordinate == (2, 3)
    assert unresolved_connectors[0].direction == Direction.South


def test_get_connector_coord(generator):
    first_connector = TestPieceOne.connectors[Direction.North][0]
    pointer_coordinate = (1, 0)
    x, y = generator._get_connector_coord(first_connector, pointer_coordinate)

    assert x == 2
    assert y == 0


def test_resolve_next_connectors(generator):
    # TODO This is huge, skipped for now
    # generator._resolve_next_connectors(
    #     cls, level, spawn_grid, unresolved_connectors)
    pass


def test_fill_empty_spaces():
    class FilledGenerator(ConnectorBasedGenerator):
        filler_tile = floors.DungeonFloor
    level = Level(50, 50)
    rejected_tiles = (
        (1, 0),
        (2, 0),
        (20, 0),
        (29, 1),
        (38, 2),
    )
    FilledGenerator._fill_empty_tiles(level, rejected_tiles)

    filled_tiles = [level.get_tile(coord) for coord in rejected_tiles]
    assert len(filled_tiles) == len(rejected_tiles)
    for tile in filled_tiles:
        assert isinstance(tile, floors.DungeonFloor)


def test_get_compatible_pieces():
    class PiecedGenerator(ConnectorBasedGenerator):
        pieces = [
            (100, TestPieceOne),
            (100, TestPieceTwo),
        ]
    origin_direction = Direction.North
    pieces = PiecedGenerator._get_compatible_pieces(
        origin_direction=origin_direction,
        connector=Connector(),
    )

    assert len(pieces) == 1
    assert TestPieceTwo in pieces


def test_all_tiles_fit_when_true(generator):
    spawn_grid = [(0,0), (0, 1), (0,2), (1,0), (1,1), (1, 2), (2,0), (2,1), (2,2)]
    origin_coord = (0, 0)
    result = generator._all_tiles_fit(TestPieceOne, spawn_grid, origin_coord)

    assert result is True


def test_all_tiles_fit_when_false(generator):
    spawn_grid = [(0, 0), (0, 1)]
    origin_coord = (0, 0)
    result = generator._all_tiles_fit(TestPieceOne, spawn_grid, origin_coord)

    assert result is False


def test_get_origin_for_new_piece_north(generator):
    connector = TestPieceTwo.connectors.get(Direction.South)[0]
    old_origin = (10, 10)
    connector_coordinate = (10, 10)
    new_origin = generator._get_origin_for_new_piece(
        direction=Direction.North,
        new_piece=TestPieceTwo,
        connector_coord=connector_coordinate,
        connector=connector,
        old_origin=old_origin
    )

    assert new_origin == (9, 7)


def test_get_origin_for_new_piece_east(generator):
    connector = TestPieceThree.connectors.get(Direction.West)[0]
    connector_coordinate = (10, 10)
    new_origin = generator._get_origin_for_new_piece(
        direction=Direction.East,
        new_piece=TestPieceThree,
        connector_coord=connector_coordinate,
        connector=connector
    )

    assert new_origin == (10, 9)
