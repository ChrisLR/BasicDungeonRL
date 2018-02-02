from services.selection.filters.base import SelectionFilter


class Conscious(SelectionFilter):
    """
    Removes all conscious game objects
    """
    def __init__(self):
        super().__init__()
        self.view = None

    def filter(self, targets):
        self.resolution = []
        for target in targets:
            if target.health:
                if target.health.conscious:
                    continue
            self.resolution.append(target)
