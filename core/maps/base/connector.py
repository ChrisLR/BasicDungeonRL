class Connector(object):
    """
    This Connector will link possible rooms together.
    """
    def __init__(self, *local_coordinates):
        self.local_coordinates = local_coordinates

    def __eq__(self, other):
        if isinstance(other, Connector):
            return type(self) == type(other)
        return False

    def __ne__(self, other):
        if isinstance(other, Connector):
            return type(self) != type(other)
        return True

    def write(self, level, origin, direction, new_piece, new_origin):
        pass

    def get_adjacent_coordinates(self, target_coordinate):
        neighbors = []
        for coordinate in self.local_coordinates:
            if coordinate != target_coordinate:
                cx, cy = coordinate
                tx, ty = target_coordinate
                if abs(cx - tx) + abs(cy - ty) < 1:
                    neighbors.append(coordinate)