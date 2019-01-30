from core.components import Component, listing


@listing.register
class Player(Component):
    NAME = "player"
    __slots__ = []
    """
    PlaceHolder Component to identify the player.
    """

    def __init__(self):
        super().__init__()

    def copy(self):
        return Player()