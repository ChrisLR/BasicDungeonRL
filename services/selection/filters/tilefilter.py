from core.tiles.base import Tile
from services.selection.filters.base import SelectionFilter


class TileExclusionFilter(SelectionFilter):
    """
    Excludes any Tiles
    """

    def filter(self, targets):
        self.resolution = [
            target for target in targets
            if not isinstance(target, Tile)
        ]
