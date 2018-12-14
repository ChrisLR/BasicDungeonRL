from core.gameobject import GameObject


class Region(GameObject):
    __slots__ = ["areas"]

    def __init__(self, game):
        super().__init__(game)
        self.areas = {}

    def add_area(self, coordinates, area):
        self.areas[coordinates] = area

    def get_area(self, coordinates):
        area = self.areas.get(coordinates, None)
        if area:
            return area
        raise Exception("No Area for coordinates {}".format(coordinates))
