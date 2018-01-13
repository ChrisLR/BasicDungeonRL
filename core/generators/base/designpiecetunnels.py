import random

from sortedcontainers import SortedSet

from core.world.room import Room
from core.generators.base.designpiece import DesignPieceGenerator


class TunneledDesignPieceGenerator(DesignPieceGenerator):
    max_amount_of_rooms = 1

    @classmethod
    def _generate(cls, level):
        spawn_grid = cls._prepare_spawn_grid(level)
        rejected_tiles = set()
        cls._place_pieces(
            level=level,
            spawn_grid=spawn_grid,
            rejected_tiles=rejected_tiles
        )
        cls._dig_tunnels(level, spawn_grid)
        rejected_tiles.update(spawn_grid)
        cls._fill_empty_spaces(level, rejected_tiles)

    @classmethod
    def _place_pieces(cls, level, spawn_grid, rejected_tiles):
        tries = cls.max_amount_of_rooms * 10
        pieces_wrote = 0
        available_pieces = cls.pieces.copy()
        while tries:
            new_piece = cls._select_piece(available_pieces)
            if not new_piece:
                return

            coords = cls._try_fit_piece(new_piece, spawn_grid, rejected_tiles)
            if coords:
                pieces_wrote += 1
                level.add_room(Room(*coords, new_piece))
                cls._write_piece(level, new_piece, spawn_grid, coords)
                if pieces_wrote >= cls.max_amount_of_rooms:
                    return
                continue
            tries -= 1

    @classmethod
    def _try_fit_piece(cls, piece, spawn_grid, rejected_tiles):
        # Random plucking coordinates, should drop rooms at random spots.
        while spawn_grid:
            index = random.randint(0, len(spawn_grid) - 1)
            new_point = spawn_grid.pop(index)
            if cls._all_tiles_fit(piece, spawn_grid, new_point):
                return new_point
            else:
                rejected_tiles.add(new_point)

        return tuple()

    @classmethod
    def _dig_tunnels(cls, level, spawn_grid):
        """
        Here, the goal is to get all room centers.

        """
        pass