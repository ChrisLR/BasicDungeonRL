from bflib.characters.classes import listing
from services.selection.base import Selection
from core.abilities.immolation import Immolation, InfiniteImmolation, SmallImmolation


class UseableAbilities(Selection):
    """
    This selects all abilities a character can use.
    """
    def __init__(self, executor):
        super().__init__(executor)
        self.view = None

    def resolve(self):
        self.resolution = [Immolation, InfiniteImmolation, SmallImmolation]