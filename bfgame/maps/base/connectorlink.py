class ConnectorLink(object):
    """
    The piece used to link a coordinate, a direction and a connector
    before it is resolved
    """
    __slots__ = ["connector", "coordinate", "origin", "direction"]

    def __init__(self, connector, coordinate, origin, direction):
        self.connector = connector
        self.coordinate = coordinate
        self.origin = origin
        self.direction = direction

    def write(self, level, new_piece, new_origin):
        self.connector.write(level, self.origin, self.direction, new_piece, new_origin)