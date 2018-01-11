import random
import collections
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
        pointer_coord = cls._get_origin_from_piece_center(center_coordinate,
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
        cls._fill_empty_tiles(level, rejected_tiles)

    @classmethod
    def _prepare_spawn_grid(cls, level):
        """
        This prepares a SortedSet containing all possible coordinates
        """
        spawn_grid = SortedSet()
        for x in range(0, level.max_x):
            for y in range(0, level.max_y):
                spawn_grid.add((x, y))

        return spawn_grid

    @classmethod
    def _get_origin_from_piece_center(cls, center_coordinate, piece):
        """
        This returns the Top Left Coordinate from a Piece and its center.
        """
        x_offset = int(piece.get_width() / 2)
        y_offset = int(piece.get_height() / 2)
        x_center, y_center = center_coordinate

        return x_center - x_offset, y_center - y_offset

    @classmethod
    def _get_center_coordinate(cls, level):
        """
        Returns the Center coordinate of a level.
        """
        return round(level.width / 2), round(level.height / 2)

    @classmethod
    def _get_pieces_by_connectors_amount(cls):
        # We shuffle to avoid duplicate counts
        # being in the same order every time.
        pieces = [
            piece for _, piece
            in cls.pieces_with_percentage if piece.connectors]
        random.shuffle(pieces)
        return sorted(
            pieces, key=lambda piece: len(piece.connectors), reverse=True)

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
            if inverse_origin_direction is not None and inverse_origin_direction == direction:
                continue

            if isinstance(connectors, collections.Iterable):
                connector = random.choice(connectors)
            else:
                connector = connectors

            unresolved_connectors.append(
                ConnectorLink(
                    connector=connector,
                    coordinate=cls._get_connector_coord(
                        connector=connector,
                        pointer_coord=pointer_coords
                    ),
                    direction=direction
                )
            )

    @classmethod
    def _get_connector_coord(cls, connector, pointer_coord):
        """
        This returns the coordinate of a connector
        """
        coordinate = random.choice(connector.possible_coordinates)
        offset_x, offset_y = coordinate
        origin_x, origin_y = pointer_coord

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
                    connector=connector_link.connector
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
    def _fill_empty_tiles(cls, level, rejected_tiles):
        """
        This method considers all empty tiles are in rejected tiles
        """
        for coordinate in rejected_tiles:
            level.add_tile(coordinate, cls.filler_tile)

    @classmethod
    def _get_compatible_pieces(cls, origin_direction, connector):
        return [
            piece for _, piece
            in cls.pieces_with_percentage
            if piece.connectors
            and connector in piece.connectors.get(
                get_inverse_direction(origin_direction), []
            )
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
    def _get_origin_for_new_piece(cls, direction, piece, connector_coord, connector):
        """
        This returns the top left coordinate
        for a room moved in a specified direction.
        We Overlap one edge with the other room to "connect" them.
        """
        width = piece.get_width()
        height = piece.get_height()
        connector_x, connector_y = connector_coord
        if Direction.North is direction:
            # When Going North
            # The X offset is the X Position of the SOUTHERN connector of the new piece
            # The Y offset is TOTAL HEIGHT -1,
            # Both offsets are SUBTRACTED
            offset_x, _ = min(connector.possible_coordinates, key=lambda coord: coord[0])
            offset_y = height
        elif Direction.South is direction:
            # When Going South
            # The X Offset is the X Position of the WESTERN connector of the new piece
            # The Y Offset is ZERO, because the NORTH side is at the same spot as the connector
            # Both offsets are SUBTRACTED
            offset_x, _ = min(connector.possible_coordinates, key=lambda coord: coord[0])
            offset_y = 0
        elif Direction.East is direction:
            # When Going East
            # The X Offset is ZERO, because the LEFT side is at the same spot as the connector
            # The Y offset is the Y Position of the WESTERN connector of the new piece
            # Both offsets are SUBTRACTED
            offset_x = 0
            _, offset_y = min(connector.possible_coordinates, key=lambda coord: coord[1])
        elif Direction.West is direction:
            # When Going West
            # The X offset is TOTAL WIDTH -1
            # The Y offset is the Y Position of the EASTERN connector of the new piece
            # Both offsets are SUBTRACTED
            offset_x = width
            _, offset_y = min(connector.possible_coordinates, key=lambda coord: coord[1])
        else:
            raise Exception("Unhandled Direction")

        return (
            connector_x - offset_x,
            connector_y - offset_y
        )


connector_offset_x_dict = {
    Direction.North: lambda piece: random.randint(1, piece.get_width()),
    Direction.South: lambda piece: random.randint(1, piece.get_width()),
    Direction.West: lambda piece: 0,
    Direction.East: lambda piece: piece.get_width()
}

connector_offset_y_dict = {
    Direction.North: lambda piece: 0,
    Direction.South: lambda piece: piece.get_height(),
    Direction.East: lambda piece: random.randint(1, piece.get_height()),
    Direction.West: lambda piece: random.randint(1, piece.get_height()),
}
