class MapPiece(object):
    name = ""
    tiles = ""
    symbolic_links = {}
    spawn_ratios = tuple()
    spawners = tuple()
    connectors = {}

    @classmethod
    def write_tiles_level(cls, level, left_x, top_y):
        local_x = 0
        local_y = 0
        for line in cls.tiles.splitlines():
            for char in line:
                tile_link = cls.symbolic_links.get(char, None)
                if tile_link:
                    world_coordinates = (left_x + local_x, top_y + local_y)
                    level.add_tile(world_coordinates, tile_link)
                else:
                    raise Exception("Char {} has no link".format(char))
                local_x += 1
            local_x = 0
            local_y += 1

    @classmethod
    def get_width(cls):
        return max([len(line) for line in cls.tiles.splitlines()])

    @classmethod
    def get_height(cls):
        return len(cls.tiles.splitlines())


class Connector(object):
    """
    This Connector will link possible rooms together.
    """
    @classmethod
    def write(cls, level, coordinate):
        pass


class ConnectorLink(object):
    """
    The piece used to link a coordinate, a direction and a connector
    before it is resolved
    """
    __slots__ = ["connector", "coordinate", "direction"]

    def __init__(self, connector, coordinate, direction):
        self.connector = connector
        self.coordinate = coordinate
        self.direction = direction

    def write(self, level):
        self.connector.write(level, self.coordinate)


def merge_connectors(*connector_dicts):
    final_dict = {}
    for connector_dict in connector_dicts:
        for direction, connectors in connector_dict:
            final_connectors = final_dict.get(direction, set())
            if isinstance(connectors, tuple):
                final_connectors.update(set(connectors))
            else:
                final_connectors.add(connectors)
            final_dict[direction] = final_connectors
