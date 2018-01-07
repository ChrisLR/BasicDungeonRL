import random

from sortedcontainers import SortedSet

from core.world.room import Room
from core.generators.maps.base import ConnectorLink
from core.direction import Direction


class DesignPieceGenerator(object):
    pieces_with_percentage = None
    filler_tile = None

    @classmethod
    def _generate(cls, level):
        spawn_grid = cls._prepare_spawn_grid(level)
        rejected_tiles = set()
        cls._place_pieces(
            level=level,
            spawn_grid=spawn_grid,
            rejected_tiles=rejected_tiles
        )
        rejected_tiles.update(spawn_grid)
        cls._fill_empty_spaces(level, rejected_tiles)

    @classmethod
    def _prepare_spawn_grid(cls, level):
        spawn_grid = SortedSet()
        for x in range(0, level.max_x):
            for y in range(0, level.max_y):
                spawn_grid.add((x, y))

        return spawn_grid

    @classmethod
    def _place_pieces(cls, level, spawn_grid, rejected_tiles):
        tries = 10
        available_pieces = cls.pieces_with_percentage.copy()
        while tries:
            new_piece = cls._select_piece(available_pieces)
            if not new_piece:
                return

            coords = cls._try_fit_piece(new_piece, spawn_grid, rejected_tiles)
            if coords:
                level.add_room(Room(*coords, new_piece))
                cls._write_piece(level, new_piece, spawn_grid, coords)
                continue
            tries -= 1

    @classmethod
    def _select_piece(cls, pieces_with_percentage):
        randomized_pieces = pieces_with_percentage.copy()
        random.shuffle(randomized_pieces)
        for percentage, piece in randomized_pieces:
            if percentage >= random.randint(0, 100):
                return piece

        return None

    @classmethod
    def _try_fit_piece(cls, piece, spawn_grid, rejected_tiles):
        while spawn_grid:
            new_point = spawn_grid.pop(0)
            if cls._all_tiles_fit(piece, spawn_grid, new_point):
                return new_point
            else:
                rejected_tiles.add(new_point)

        return False

    @classmethod
    def _all_tiles_fit(cls, piece, spawn_grid, offset_coords):
        offset_x, offset_y = offset_coords
        for piece_x in range(0, piece.get_width()):
            for piece_y in range(0, piece.get_height()):
                tile_coords = (piece_x + offset_x, piece_y + offset_y)
                if tile_coords not in spawn_grid:
                    if tile_coords != offset_coords:
                        return False

        return True

    @classmethod
    def _write_piece(cls, level, piece, spawn_grid, pointer_coords):
        pointer_x, pointer_y = pointer_coords
        for x in range(pointer_x, pointer_x + piece.get_width()):
            for y in range(pointer_y, pointer_y + piece.get_height()):
                new_point = (x, y)
                if new_point != pointer_coords:
                    spawn_grid.remove(new_point)

        piece.write_tiles_level(level, pointer_x, pointer_y)
        for spawner in piece.spawners:
            for spawned_object in spawner.spawn(offset_coords=(pointer_x, pointer_y)):
                level.add_object(spawned_object)

    @classmethod
    def _fill_empty_spaces(cls, level, rejected_tiles):
        for coordinate in rejected_tiles:
            level.add_tile(coordinate, cls.filler_tile)


class ConnectorBasedGenerator(object):
    """
    Get the Center Coordinate
    Order pieces by connectors amount
    Get the piece with the most connectors, random between ties.
    Write the Piece and iterate through connectors.
    Each Connector selects a compatible room and write it
    Each of those rooms are added into a list.
    This list is then iterated and all THEIR connectors are written,
    adding these new rooms to a new list to do the same.
    It should write each step in all directions at a time.
    """

    pieces_with_percentage = None
    filler_tile = None

    @classmethod
    def _generate(cls, level):
        spawn_grid = cls._prepare_spawn_grid(level)
        rejected_tiles = set()
        unresolved_connectors = []

        center_coordinate = cls._get_center_coordinate(level)
        ordered_pieces = cls._get_pieces_by_connectors_amount()
        central_piece = ordered_pieces[0]
        pointer_coord = cls._position_cursor_from_room_center(center_coordinate, central_piece)
        cls._write_piece(
            level=level,
            piece=central_piece,
            spawn_grid=spawn_grid,
            pointer_coords=pointer_coord,
            unresolved_connectors=unresolved_connectors
        )

        rejected_tiles.update(spawn_grid)
        cls._fill_empty_spaces(level, rejected_tiles)

    @classmethod
    def _prepare_spawn_grid(cls, level):
        spawn_grid = SortedSet()
        for x in range(0, level.max_x):
            for y in range(0, level.max_y):
                spawn_grid.add((x, y))

        return spawn_grid

    @classmethod
    def _position_cursor_from_room_center(cls, center_coordinate, piece):
        x_offset = round(piece.get_width() / 2)
        y_offset = round(piece.get_height() / 2)
        x_center, y_center = center_coordinate

        return x_center - x_offset, y_center - y_offset

    @classmethod
    def _get_center_coordinate(cls, level):
        return round(level.width / 2), round(level.height / 2)

    @classmethod
    def _get_pieces_by_connectors_amount(cls):
        # We shuffle to avoid duplicate counts
        # being in the same order every time.
        shuffled_pieces = random.shuffle(
            [piece for _, piece in cls.pieces_with_percentage]
        )
        return sorted(shuffled_pieces, key=lambda piece: len(piece.connectors))

    @classmethod
    def _write_piece(cls, level, piece, spawn_grid,
                     pointer_coords, unresolved_connectors):

        cls._add_unresolved_connectors(
            piece, pointer_coords, unresolved_connectors
        )
        pointer_x, pointer_y = pointer_coords
        for x in range(pointer_x, pointer_x + piece.get_width()):
            for y in range(pointer_y, pointer_y + piece.get_height()):
                new_point = (x, y)
                if new_point != pointer_coords:
                    spawn_grid.remove(new_point)

        piece.write_tiles_level(level, pointer_x, pointer_y)
        for spawner in piece.spawners:
            for spawned_object in spawner.spawn(
                    offset_coords=(pointer_x, pointer_y)):
                level.add_object(spawned_object)

    @classmethod
    def _add_unresolved_connectors(
            cls, piece, pointer_coords, unresolved_connectors):
        for direction, connectors in piece.connectors.items():
            unresolved_connectors.append(
                ConnectorLink(
                    connector=random.choice(connectors),
                    coordinate=cls._get_connector_coord_from_direction(
                        direction=direction,
                        piece=piece, # TODO THIS MUST INSTEAD SELECT A COMPATIBLE PIECE
                        pointer_coord=pointer_coords
                    ),
                    direction=direction
                )
            )

    @classmethod
    def _get_connector_coord_from_direction(
            cls, direction, piece, pointer_coord):
        # The pointer coord here must refer to the top left.
        origin_x, origin_y = pointer_coord
        offset_x = connector_offset_x_dict[direction](piece)
        offset_y = connector_offset_y_dict[direction](piece)

        return origin_x + offset_x, origin_y + offset_y

    @classmethod
    def _resolve_next_connectors(cls):
        """
        Here we must get all connectors currently in the list
        We copy this list and empty it so any future
        connectors will not be evaluated for this step.

        Then we iterate upon our copy and resolve each connector.
        This includes making sure the piece fits, writing the connector,
        writing the piece, adding every connectors
        that is not the origin direction.

        The order is important, if the piece did not fit we do not add
        it's connectors so it will naturally stop once
        we reach the edge of the map.
        :return:
        """

    @classmethod
    def _fill_empty_spaces(cls, level, rejected_tiles):
        for coordinate in rejected_tiles:
            level.add_tile(coordinate, cls.filler_tile)


connector_offset_x_dict = {
    Direction.North: lambda piece: random.randint(1, piece.get_width() - 1),
    Direction.South: lambda piece: random.randint(1, piece.get_width() - 1),
    Direction.West: lambda piece: 0,
    Direction.East: lambda piece: piece.get_width()
}

connector_offset_y_dict = {
    Direction.North: lambda piece: 0,
    Direction.South: lambda piece: piece.get_height(),
    Direction.East: lambda piece: random.randint(1, piece.get_height() - 1),
    Direction.West: lambda piece: random.randint(1, piece.get_height() - 1),
}
