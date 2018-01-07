import random

from sortedcontainers import SortedSet

from core.world.room import Room


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


class ConnectorBasedGenerator(DesignPieceGenerator):
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

    @classmethod
    def _generate(cls, level):
        spawn_grid = cls._prepare_spawn_grid(level)
        rejected_tiles = set()
        unresolved_connectors = []

        center_coordinate = cls._get_center_coordinate(level)
        ordered_pieces = cls._get_pieces_by_connectors_amount()
        central_piece = ordered_pieces[0]
        pointer_coord = cls._position_cursor_from_room_center(center_coordinate, central_piece)
        cls._write_piece()

        rejected_tiles.update(spawn_grid)
        cls._fill_empty_spaces(level, rejected_tiles)

    @classmethod
    def _position_cursor_from_room_center(cls, center_coordinate, piece):
        x_offset = round(piece.get_width() / 2)
        y_offset = round(piece.get_height() / 2)
        x_center, y_center = center_coordinate

        return x_center - x_offset, y_center - y_offset

    @classmethod
    def _write_piece(cls, level, piece, spawn_grid, pointer_coords):

    @classmethod
    def _get_center_coordinate(cls, level):
        return round(level.width / 2), round(level.height / 2)

    @classmethod
    def _get_pieces_by_connectors_amount(cls):
        # We shuffle to avoid duplicate counts being in the same order every time.
        shuffled_pieces = random.shuffle(
            [piece for _, piece in cls.pieces_with_percentage]
        )
        return sorted(shuffled_pieces, key=lambda piece: len(piece.connectors))

