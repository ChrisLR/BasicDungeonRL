from core.abilities import Hide, OpenLock, PickPocket, RemoveTraps
from core.abilities.immolation import Immolation, InfiniteImmolation, SmallImmolation
from services.selection.base import Selection


class UseableAbilities(Selection):
    """
    This selects all abilities a character can use.
    """
    def resolve(self):
        self.resolution = [Immolation, InfiniteImmolation, SmallImmolation, Hide, OpenLock, PickPocket, RemoveTraps]
