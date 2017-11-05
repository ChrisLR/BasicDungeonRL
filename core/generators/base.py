import random


class DesignPieceGenerator(object):
    """
    This needs a list of pieces to generate from with percentages to generate
    It needs to randomize these pieces and place them on a grid with a fixed width/height.
    The first piece set is placed down based on the percentage success, then
    We drop down and try to find another piece that fits in the designated area.
    We roll for percentage and place.
    If nothing fits anymore we go back to Y zero with X + maximum piece Width
    """
    pieces_with_percentage = None
    filler_tile = None

    @classmethod
    def _generate(cls, level):
        spawn_grid = {}
        tries = 10
        available_pieces = cls.pieces_with_percentage.copy()
        while tries:
            new_piece = cls._select_piece(available_pieces)
            if not new_piece:
                return

            coords = cls._try_fit_piece(level, new_piece, spawn_grid)
            if coords:
                cls._write_piece(spawn_grid, level, new_piece, coords)
                continue
            tries -= 1

        cls._fill_empty_spaces(level, spawn_grid)

    @classmethod
    def _fill_empty_spaces(cls, level, spawn_grid):
        for x in range(0, level.max_x):
            for y in range(0, level.max_y):
                if (x, y) not in spawn_grid:
                    level.add_tile((x, y), cls.filler_tile)

    @classmethod
    def _select_piece(cls, pieces_with_percentage):
        randomized_pieces = pieces_with_percentage.copy()
        random.shuffle(randomized_pieces)
        for percentage, piece in randomized_pieces:
            if percentage >= random.randint(0, 100):
                return piece

        return None

    @classmethod
    def _write_piece(cls, spawn_grid, level, piece, pointer_coords):
        pointer_x, pointer_y = pointer_coords
        for x in range(pointer_x, pointer_x + piece.get_width()):
            for y in range(pointer_y, pointer_y + piece.get_height()):
                spawn_grid[(x, y)] = False

        piece.write_tiles_level(level, pointer_x, pointer_y)
        for spawner in piece.spawners:
            for spawned_object in spawner.spawn(offset_coords=(pointer_x, pointer_y)):
                level.add_object(spawned_object)

    @classmethod
    def _try_fit_piece(cls, level, piece, spawn_grid):
        piece_height = piece.get_height()
        piece_width = piece.get_width()
        pointer_x = 0
        pointer_y = 0
        while pointer_x + piece_width < level.max_x:
            empty_space = spawn_grid.get((pointer_x, pointer_y), True)
            if empty_space:
                piece_fits = cls._check_if_all_tiles_fit(
                    spawn_grid, piece_height, piece_width, (pointer_x, pointer_y))

                if piece_fits:
                    return pointer_x, pointer_y

            pointer_y += 1
            if pointer_y + piece_height > level.max_y:
                pointer_y = 0
                pointer_x += 1

        return False

    @classmethod
    def _check_if_all_tiles_fit(cls, spawn_grid, piece_height, piece_width, offset_coords):
        offset_x, offset_y = offset_coords
        for piece_x in range(0, piece_width):
            for piece_y in range(0, piece_height):
                tile_coords = (piece_x + offset_x, piece_y + offset_y)
                if not spawn_grid.get(tile_coords, True):
                    return False

        return True
