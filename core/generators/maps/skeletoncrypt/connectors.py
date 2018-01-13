from core.generators.maps.base import Connector
from core.tiles import doors, floors
from core.direction import move_direction_mapping, get_inverse_direction


class DungeonDoorConnectorA(Connector):
    # TODO A nice touch here would be to sometimes generate
    # TODO A rusty/locked door, requiring bashing/picking

    def write(self, level, origin, direction, new_piece, new_origin):
        inverse_direction = get_inverse_direction(direction)
        origin_x, origin_y = origin
        new_origin_x, new_origin_y = new_origin
        compatible_connector = next(
            (connector for connector
             in new_piece.connectors.get(inverse_direction)
             if isinstance(connector, type(self))))
        other_neighbors = compatible_connector.local_coordinates
        real_other_neighbors = [
            (x + new_origin_x, y + new_origin_y)
            for x, y in other_neighbors]

        real_neighbors = [
            (x + origin_x, y + origin_y)
            for x, y in self.local_coordinates]
        offset_x, offset_y = move_direction_mapping.get(direction)
        confirmed_neighbors = set()
        confirmed_other_neighbors = set()
        for neighbor_x, neighbor_y in real_neighbors:
            target_neighbor = (neighbor_x + offset_x, neighbor_y + offset_y)
            if target_neighbor in real_other_neighbors:
                confirmed_neighbors.add((neighbor_x, neighbor_y))
                confirmed_other_neighbors.add(target_neighbor)

        for coordinate in confirmed_neighbors:
            level.add_tile(coordinate, doors.DungeonDoor())

        for coordinate in confirmed_other_neighbors:
            level.add_tile(coordinate, floors.DungeonFloor())


class DungeonFloorConnectorA(Connector):
    def write(self, level, origin, direction, new_piece, new_origin):
        inverse_direction = get_inverse_direction(direction)
        origin_x, origin_y = origin
        new_origin_x, new_origin_y = new_origin
        compatible_connector = next(
            (connector for connector
             in new_piece.connectors.get(inverse_direction)
             if isinstance(connector, type(self))))
        other_neighbors = compatible_connector.local_coordinates
        real_other_neighbors = [
            (x + new_origin_x, y + new_origin_y)
            for x, y in other_neighbors]

        real_neighbors = [
            (x + origin_x, y + origin_y)
            for x, y in self.local_coordinates]
        offset_x, offset_y = move_direction_mapping.get(direction)
        confirmed_neighbors = set()
        confirmed_other_neighbors = set()
        for neighbor_x, neighbor_y in real_neighbors:
            target_neighbor = (neighbor_x + offset_x, neighbor_y + offset_y)
            if target_neighbor in real_other_neighbors:
                confirmed_neighbors.add((neighbor_x, neighbor_y))
                confirmed_other_neighbors.add(target_neighbor)

        for coordinate in confirmed_neighbors:
            level.add_tile(coordinate, floors.DungeonFloor())

        for coordinate in confirmed_other_neighbors:
            level.add_tile(coordinate, floors.DungeonFloor())
