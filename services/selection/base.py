from collections import abc, Sequence


class Selection(object):
    def __init__(self, game, executor, parent_selection_set):
        self.game = game
        self.executor = executor
        self.parent_selection_set = parent_selection_set
        self.resolution = None
        self.canceled = False
        self.view = None

    def resolve(self):
        """
        This is the initialization of the Selection Resolution.
        It should push its view to the director and pop itself as soon as it is resolved.
        """
        pass


class TargetSelectionSet(object):
    """
    A Set of Target Selection
    """
    def __bool__(self):
        return bool(self.targets)

    def __len__(self):
        return len(self.selections)

    def __iter__(self):
        for target in self.targets:
            yield target

    def __getitem__(self, item):
        if isinstance(self.targets, Sequence):
            return self.targets[item]
        else:
            if item == 0:
                return self.targets

        raise TypeError()

    __slots__ = ("selections", "filters", "name", "parent_chain", "targets")

    def __init__(self, selections, filters=None, name=None, targets=None, parent_chain=None):
        """
        Represent a Set of Selections and filters, may be named.
        :param selections: Selections to apply, will be converted if single
        :param filters: Optional filters to apply on selections result
        :param name: Name of the Set
        :param parent_chain: Parent TargetChain if present.
        :param targets: Result of the selections and filters
        """
        if not isinstance(selections, abc.Iterable):
            selections = [selections]

        if filters is not None:
            if not isinstance(filters, abc.Iterable):
                filters = [filters]

        self.selections = selections
        self.filters = filters if filters else []
        self.targets = targets if targets else []
        self.name = name
        self.parent_chain = parent_chain

    def copy(self):
        return TargetSelectionSet(
            self.selections,
            self.filters,
            self.name,
            self.targets,
        )


class TargetSelectionChain(abc.Sequence):
    """
    Named Chain of Target Selections
    """

    def __len__(self):
        return len(self.target_selection_sets)

    def __init__(self, *target_selection_sets):
        self.target_selection_sets = target_selection_sets
        for target_selection_set in self.target_selection_sets:
            target_selection_set.parent_chain = self

        self._mapping = {
            target_selection_set.name: target_selection_set
            for target_selection_set in self.target_selection_sets
            if target_selection_set.name
        }

    def __iter__(self):
        for target_selection_set in self.target_selection_sets:
            yield target_selection_set

    def __getitem__(self, item):
        return self.target_selection_sets[item]

    def get(self, name):
        return self._mapping.get(name)

    def copy(self):
        copies_of_sets = [
            target_selection_set.copy()
            for target_selection_set
            in self.target_selection_sets]

        return TargetSelectionChain(*copies_of_sets)
