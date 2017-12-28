from core.generators.maps.base import Connector
from core.tiles import doors, floors


class DungeonDoorConnectorA(Connector):
    # TODO A nice touch here would be to sometimes generate
    # TODO A rusty/locked door, requiring bashing/picking

    @classmethod
    def write(cls, level, coordinate):
        level.add_tile(coordinate, doors.DungeonDoor())


class DungeonFloorConnectorA(Connector):
    @classmethod
    def write(cls, level, coordinate):
        level.add_tile(coordinate, floors.DungeonFloor())
