import collections
import random

from sortedcontainers import SortedSet

from core.direction import (
    Direction, get_inverse_direction
)
from bfgame.maps.base.connectorlink import ConnectorLink
from core.world import Room


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

    pieces = None
    filler_tile = None
    max_amount_of_rooms = 1

    def __init__(self, game):
        self.game = game

    def _generate(self, level):
        spawn_grid = self._prepare_spawn_grid(level)
        rejected_tiles = set()
        unresolved_connectors = []

        center_coordinate = self._get_center_coordinate(level)
        ordered_pieces = self._get_pieces_by_connectors_amount()
        central_piece = ordered_pieces[0]
        pointer_coord = self._get_origin_from_piece_center(
            center_coordinate, central_piece)
        self._write_piece(
            level=level,
            piece=central_piece,
            spawn_grid=spawn_grid,
            origin=pointer_coord,
            unresolved_connectors=unresolved_connectors
        )
        while unresolved_connectors:
            if len(level.rooms) >= self.max_amount_of_rooms:
                break
            self._resolve_next_connectors(
                level=level,
                spawn_grid=spawn_grid,
                unresolved_connectors=unresolved_connectors,
            )

        rejected_tiles.update(spawn_grid)
        self._fill_empty_tiles(level, rejected_tiles)

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
            piece_spawn.map_piece for piece_spawn
            in cls.pieces if piece_spawn.map_piece.connectors]
        random.shuffle(pieces)
        return sorted(
            pieces, key=lambda piece: len(piece.connectors), reverse=True)

    def _write_piece(
            self, level, piece, spawn_grid, origin,
            unresolved_connectors, origin_direction=None):

        level.add_room(Room(*origin, piece))
        self._add_unresolved_connectors(
            piece=piece,
            origin=origin,
            unresolved_connectors=unresolved_connectors,
            origin_direction=origin_direction
        )

        pointer_x, pointer_y = origin
        for x in range(pointer_x, pointer_x + piece.get_width()):
            for y in range(pointer_y, pointer_y + piece.get_height()):
                new_point = (x, y)
                if new_point in spawn_grid:
                    spawn_grid.remove(new_point)

        piece.write_tiles_level(level, pointer_x, pointer_y)
        for spawner in piece.spawners:
            for spawned_object in spawner.spawn(self.game, origin=(pointer_x, pointer_y)):
                level.add_object(spawned_object)

    @classmethod
    def _add_unresolved_connectors(
            cls, piece, origin,
            unresolved_connectors, origin_direction=None):

        inverse_origin_direction = (
            get_inverse_direction(origin_direction)
            if origin_direction is not None else None
        )
        for direction, connectors in piece.connectors.items():
            if (inverse_origin_direction is not None
                    and inverse_origin_direction == direction):
                continue

            if isinstance(connectors, collections.Iterable):
                connector = random.choice(connectors)
            else:
                connector = connectors
            
            unresolved_connectors.append(
                ConnectorLink(
                    connector=connector,
                    coordinate=cls._get_connector_coord(connector, direction, origin),
                    origin=origin,
                    direction=direction
                )
            )

    @classmethod
    def _get_connector_coord(cls, connector, direction, origin):
        """
        This returns the coordinate of a connector
        """
        coordinate = min(connector.local_coordinates)
        offset_x, offset_y = coordinate
        origin_x, origin_y = origin

        return origin_x + offset_x, origin_y + offset_y

    def _resolve_next_connectors(self, level, spawn_grid, unresolved_connectors):
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
            compatible_pieces = self._get_compatible_pieces(
                origin_direction=connector_link.direction,
                connector=connector_link.connector
            )
            compatible_pieces = self.filter_map_pieces_by_amounts(level, compatible_pieces)
            while compatible_pieces:
                piece_spawn = compatible_pieces.pop(0)
                chance = random.randint(0, 100)
                if chance > piece_spawn.chance:
                    continue

                piece = piece_spawn.map_piece
                new_origin_coord = self._get_origin_for_new_piece(
                    direction=connector_link.direction,
                    new_piece=piece,
                    connector_coord=connector_link.coordinate,
                    connector=connector_link.connector,
                    old_origin=connector_link.origin
                )
                if self._all_tiles_fit(piece, spawn_grid, new_origin_coord):
                    self._write_piece(
                        level=level,
                        piece=piece,
                        spawn_grid=spawn_grid,
                        origin=new_origin_coord,
                        unresolved_connectors=unresolved_connectors,
                        origin_direction=connector_link.direction,
                    )
                    connector_link.write(level, piece, new_origin_coord)
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
        compatible_pieces = [
            piece_spawn for piece_spawn in cls.pieces
            if piece_spawn.map_piece.connectors
            and connector in piece_spawn.map_piece.connectors.get(
                get_inverse_direction(origin_direction), []
            )
        ]

        return compatible_pieces

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
    def _get_origin_for_new_piece(cls, direction, new_piece, connector_coord, connector, old_origin):
        """
        This returns the top left coordinate
        for a room moved in a specified direction.
        """
        width = new_piece.get_width()
        height = new_piece.get_height()
        # TODO This is ugly, clean this
        new_connector = next(
            (n_connector for n_connector
             in new_piece.connectors.get(get_inverse_direction(direction))
             if type(n_connector) == type(connector)))

        connector_x, connector_y = connector_coord
        old_origin_x, old_origin_y = old_origin
        local_connector_x = connector_x - old_origin_x
        local_connector_y = connector_y - old_origin_y

        if Direction.North is direction:
            minimal_x, _ = min(new_connector.local_coordinates,
                               key=lambda coordinate: coordinate[0])
            offset_x = local_connector_x - minimal_x
            offset_y = -height
        elif Direction.South is direction:
            minimal_x, _ = min(new_connector.local_coordinates,
                               key=lambda coordinate: coordinate[0])
            offset_x = local_connector_x - minimal_x
            offset_y = local_connector_y + 1
        elif Direction.East is direction:
            offset_x = local_connector_x + 1
            _, minimal_y = min(new_connector.local_coordinates,
                               key=lambda coordinate: coordinate[1])
            offset_y = local_connector_y - minimal_y
        elif Direction.West is direction:
            offset_x = -width
            _, minimal_y = min(new_connector.local_coordinates,
                               key=lambda coordinate: coordinate[1])
            offset_y = local_connector_y - minimal_y
        else:
            raise Exception("Unhandled Direction")

        return (
            old_origin_x + offset_x,
            old_origin_y + offset_y
        )

    @classmethod
    def filter_map_pieces_by_amounts(cls, level, map_pieces):
        pieces_with_amounts = []
        for map_piece_spawn in map_pieces:
            amount = len([room for room in level.rooms if room.design_piece == map_piece_spawn.map_piece])
            if map_piece_spawn.spawn_limit is None:
                pieces_with_amounts.append((amount, map_piece_spawn))
            elif amount < map_piece_spawn.spawn_limit:
                pieces_with_amounts.append((amount, map_piece_spawn))

        pieces_with_amounts = sorted(pieces_with_amounts, key=lambda piece: piece[0])

        return [piece for _, piece in pieces_with_amounts]
