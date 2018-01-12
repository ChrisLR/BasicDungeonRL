from core.generators.maps.base import Connector
from core.tiles import doors, floors
from core.direction import move_direction_mapping


class DungeonDoorConnectorA(Connector):
    # TODO A nice touch here would be to sometimes generate
    # TODO A rusty/locked door, requiring bashing/picking

    def write(self, level, coordinate, direction):
        # TODO Neighbor Coordinates are NOT real world positions
        # TODO We need the ORIGIN to write them.
        cx, cy = coordinate
        ox, oy = move_direction_mapping.get(direction)
        off_x = ox + cx
        off_y = oy + cy

        level.add_tile(coordinate, doors.DungeonDoor())
        level.add_tile((off_x, off_y), floors.DungeonFloor())
        for neighbor in self.possible_coordinates:
            nx, ny = neighbor
            off_x = nx + cx
            off_y = ny + cy
            level.add_tile(neighbor, doors.DungeonDoor())
            level.add_tile((off_x, off_y), floors.DungeonFloor())


class DungeonFloorConnectorA(Connector):
    def write(self, level, coordinate, direction):
        cx, cy = coordinate
        ox, oy = move_direction_mapping.get(direction)
        off_x = ox + cx
        off_y = oy + cy
        level.add_tile(coordinate, floors.DungeonFloor())
        level.add_tile((off_x, off_y), floors.DungeonFloor())
        for neighbor in self.possible_coordinates:
            nx, ny = neighbor
            off_x = nx + cx
            off_y = ny + cy
            level.add_tile(neighbor, floors.DungeonFloor())
            level.add_tile((off_x, off_y), floors.DungeonFloor())
