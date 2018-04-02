from services.selection.filters.base import SelectionFilter


class Component(SelectionFilter):
    """
    A Selection Filter using components.
    """
    component = None

    def filter(self, targets):
        if self.component is None:
            raise NotImplementedError()
        self.resolution = [target for target in targets if getattr(target, self.component.NAME)]
