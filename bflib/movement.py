import units


class MovementSet(object):
    __slots__ = ["walk", "swim", "fly", "turning_distance"]

    def __init__(self, walk, swim=None, fly=None, turning_distance=None):
        self.walk = walk  # type: units.FeetPerGameTurn
        self.swim = swim  # type: units.FeetPerGameTurn
        self.fly = fly  # type: units.FeetPerGameTurn
        self.turning_distance = turning_distance  # type: units.Feet
