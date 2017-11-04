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

    @classmethod
    def _generate(cls, level):
        spawn_grid = {}
        tries = 100
        available_pieces = cls.pieces_with_percentage.copy()
        while tries:
            new_piece = cls._select_piece(available_pieces)
            if not new_piece:
                return

            coords = cls._try_fit_piece(level, new_piece, spawn_grid)
            if coords:
                cls._write_piece(spawn_grid, level, new_piece, coords)
            tries -= 1

    @staticmethod
    def _select_piece(pieces_with_percentage):
        randomized_pieces = pieces_with_percentage.copy()
        random.shuffle(randomized_pieces)
        for percentage, piece in randomized_pieces:
            if percentage >= random.randint(0, 100):
                return piece

        return None

    @staticmethod
    def _write_piece(spawn_grid, level, piece, pointer_coords):
        pointer_x, pointer_y = pointer_coords
        for x in range(pointer_x, pointer_x + piece.get_width()):
            for y in range(pointer_y, pointer_y + piece.get_height()):
                spawn_grid[(x, y)] = False

        piece.write_tiles_level(level, pointer_x, pointer_y)
        for spawner in piece.spawners:
            for spawned_object in spawner.spawn():
                level.add_object(spawned_object)

    @staticmethod
    def _try_fit_piece(level, piece, spawn_grid):
        piece_height = piece.get_height()
        piece_width = piece.get_width()
        pointer_x = 0
        pointer_y = 0
        while pointer_x + piece_width < level.max_x:
            if pointer_y + piece_height > level.max_y:
                pointer_y = 0
                pointer_x += 1

            empty_space = spawn_grid.get((pointer_x, pointer_y), True)
            pointer_y += 1
            if empty_space:
                return pointer_x, pointer_y

        return False



