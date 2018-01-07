import random

from sortedcontainers import SortedSet

from core.direction import (
    Direction, get_inverse_direction, move_direction_mapping
)
from core.generators.maps.base import ConnectorLink
from core.world.room import Room


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
        pointer_coord = cls._position_cursor_from_room_center(center_coordinate,
                                                              central_piece)
        cls._write_piece(
            level=level,
            piece=central_piece,
            spawn_grid=spawn_grid,
            pointer_coords=pointer_coord,
            unresolved_connectors=unresolved_connectors
        )
        while unresolved_connectors:
            cls._resolve_next_connectors(
                level=level,
                spawn_grid=spawn_grid,
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
        pieces = [
            piece for _, piece
            in cls.pieces_with_percentage if piece.connectors]
        random.shuffle(pieces)
        return sorted(pieces, key=lambda piece: len(piece.connectors))

    @classmethod
    def _write_piece(
            cls, level, piece, spawn_grid, pointer_coords,
            unresolved_connectors, origin_direction=None):

        level.add_room(Room(*pointer_coords, piece))
        cls._add_unresolved_connectors(
            piece=piece,
            pointer_coords=pointer_coords,
            unresolved_connectors=unresolved_connectors,
            origin_direction=origin_direction
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
            cls, piece, pointer_coords,
            unresolved_connectors, origin_direction=None):

        inverse_origin_direction = (
            get_inverse_direction(origin_direction)
            if origin_direction is not None else None
        )
        for direction, connectors in piece.connectors.items():
            if inverse_origin_direction == direction:
                continue

            unresolved_connectors.append(
                ConnectorLink(
                    connector=random.choice(connectors),
                    coordinate=cls._get_connector_coord_from_direction(
                        direction=direction,
                        piece=piece,
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
    def _resolve_next_connectors(
            cls, level, spawn_grid, unresolved_connectors):
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
        """
        step_connectors = unresolved_connectors.copy()
        unresolved_connectors.clear()
        for connector_link in step_connectors:
            compatible_pieces = cls._get_compatible_pieces(
                origin_direction=connector_link.direction,
                connector=connector_link.connector
            )

            random.shuffle(compatible_pieces)
            while compatible_pieces:
                piece = compatible_pieces.pop(0)
                new_origin_coord = cls._get_origin_for_new_piece(
                    direction=connector_link.direction,
                    piece=piece,
                    connector_coord=connector_link.coordinate,
                )
                if cls._all_tiles_fit(piece, spawn_grid, new_origin_coord):
                    cls._write_piece(
                        level=level,
                        piece=piece,
                        spawn_grid=spawn_grid,
                        pointer_coords=new_origin_coord,
                        unresolved_connectors=unresolved_connectors,
                        origin_direction=connector_link.direction,
                    )
                    connector_link.write(level)
                    break

    @classmethod
    def _fill_empty_spaces(cls, level, rejected_tiles):
        for coordinate in rejected_tiles:
            level.add_tile(coordinate, cls.filler_tile)

    @classmethod
    def _get_compatible_pieces(cls, origin_direction, connector):
        return [
            piece for _, piece
            in cls.pieces_with_percentage
            if piece.connectors.get(
                get_inverse_direction(origin_direction)
            ) is connector
        ]

    @classmethod
    def _all_tiles_fit(cls, piece, spawn_grid, origin_coord):
        offset_x, offset_y = origin_coord
        for piece_x in range(0, piece.get_width()):
            for piece_y in range(0, piece.get_height()):
                tile_coords = (piece_x + offset_x, piece_y + offset_y)
                if tile_coords not in spawn_grid:
                    if tile_coords != origin_coord:
                        return False

        return True

    @classmethod
    def _get_origin_for_new_piece(cls, direction, piece, connector_coord):
        """
        This returns the top left coordinate
        for a room moved in a specified direction.
        We Overlap one edge with the other room to "connect" them.
        """
        inverse_direction = get_inverse_direction(direction)
        x_dir, y_dir = move_direction_mapping.get(direction)
        x_negative, y_negative = move_direction_mapping.get(inverse_direction)
        width = piece.get_width()
        height = piece.get_height()
        offset_x = x_dir * width
        offset_y = y_dir * height
        connector_x, connector_y = connector_coord

        return (
            connector_x + offset_x + x_negative,
            connector_y + offset_y + y_negative
        )


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
