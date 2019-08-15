from services.selection.filters.base import SelectionFilter


class Conscious(SelectionFilter):
    """
    Removes all conscious game objects
    """
    def filter(self, targets):
        self.resolution = []
        for target in targets:
            if target.health:
                if target.health.conscious:
                    continue
            self.resolution.append(target)


class NotConscious(SelectionFilter):
    """
    Removes all unconscious game objects
    """
    def filter(self, targets):
        self.resolution = []
        for target in targets:
            if target.health:
                if target.health.conscious:
                    self.resolution.append(target)
