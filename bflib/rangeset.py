class RangeSet(object):
    __slots__ = ["short", "medium", "long"]

    def __init__(self, short=None, medium=None, long=None):
        """
        A set defining the ranges.
        A NoneValue indicate it is impossible to get this range's bonus.
        A distance under specified range applies a modifier.
        :param short: Short Range (+1)
        :param medium: Medium Range (+0)
        :param long: Long Range (-1)
        """

        self.short = short
        self.medium = medium
        self.long = long
