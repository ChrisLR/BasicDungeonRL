from core.maps.base.connector import Connector
from core.tiles import doors, floors


class DungeonDoorConnectorA(Connector):
    # TODO A nice touch here would be to sometimes generate
    # TODO A rusty/locked door, requiring bashing/picking

    def write(self, level, origin, direction, new_piece, new_origin):
        confirmed_coordinates = set()
        confirmed_other_coordinates = set()
        level_coordinates = self.get_level_coordinates(origin)
        for lx, ly in level_coordinates:
            opposite_coordinate = self.get_opposite_level_coordinate((lx, ly), direction)
            if level.get_tile(opposite_coordinate):
                confirmed_coordinates.add((lx, ly))
                confirmed_other_coordinates.add(opposite_coordinate)

        for level_coordinate in confirmed_coordinates:
            level.add_tile(level_coordinate, doors.DungeonDoor())

        for level_coordinate in confirmed_other_coordinates:
            level.add_tile(level_coordinate, floors.DungeonFloor())


class DungeonFloorConnectorA(Connector):
    def write(self, level, origin, direction, new_piece, new_origin):
        confirmed_coordinates = set()
        confirmed_other_coordinates = set()
        level_coordinates = self.get_level_coordinates(origin)
        for lx, ly in level_coordinates:
            opposite_coordinate = self.get_opposite_level_coordinate((lx, ly), direction)
            if level.get_tile(opposite_coordinate):
                confirmed_coordinates.add((lx, ly))
                confirmed_other_coordinates.add(opposite_coordinate)

        for level_coordinate in confirmed_coordinates:
            level.add_tile(level_coordinate, floors.DungeonFloor())

        for level_coordinate in confirmed_other_coordinates:
            level.add_tile(level_coordinate, floors.DungeonFloor())
