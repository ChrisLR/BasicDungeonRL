from services.selection.filters.base import SelectionFilter
from bfgame.flags import GameObjectFlags


class ExcludeItemFlags(SelectionFilter):
    """
    Removes all game objects flagged as "item"
    """
    def filter(self, targets):
        self.resolution = []
        for target in targets:
            if GameObjectFlags.Item in target.flags:
                continue
            self.resolution.append(target)
