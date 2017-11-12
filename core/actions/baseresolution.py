from core.actions.base import Action
from core.gameobject import GameObject


class ActionResolution(object):
    """
    An object tracking an action's target resolution.
    """
    __slots__ = ["action", "executor", "selections", "pending_filters", "targets"]

    def __init__(self, action, executor):
        """
        Filters and Selections will be instantiated to be resolved.
        Result of which are stored in targets list.

        :param action: The Action to execute
        :type action: Action
        :param executor: The Executor GameObject
        :type executor: GameObject
        """

        self.action = action
        self.executor = executor
        self.targets = []
        if action.target_filters:
            self.pending_filters = [target_filter() for target_filter in action.target_filters]
        else:
            self.pending_filters = None

        if action.target_selection_types:
            self.selections = [selection(executor) for selection in action.target_selection_types]
            self._start_next_selection()
        else:
            self.selections = None

    def update(self):
        """
        Updates the selection and filter resolutions.
        """
        if self.selections:
            resolution = self.selections[-1].resolution
            if resolution:
                self.targets.extend(resolution)
                self.selections.pop(-1)
                if self.selections:
                    self._start_next_selection()
                else:
                    self._start_next_filter()


        else:
            if self.pending_filters:
                self._update_filter()

    @property
    def can_execute_action(self):
        """
        Checks if current action can be executed with resolved targets.
        """
        if self.action.can_execute(self.executor, self.targets):
            return True
        return False

    def execute_action(self):
        """
        Executes action with resolved targets.
        """
        self.action.execute(self.executor, self.targets)

    @property
    def finished_selection(self):
        """
        Determines if the selection phase is finished.
        :return: bool
        """

        return not self.selections

    @property
    def finished_filter(self):
        """
        Determines if the filter phase is finished.
        :return: bool
        """
        return not self.pending_filters

    def _update_filter(self):
        """
        Updates top of the stack filter resolution.
        """
        current_filter = self.pending_filters[-1]
        if current_filter.resolution:
            self.targets = current_filter.resolution
            self.pending_filters.pop(-1)
            self._start_next_filter()

    def _start_next_filter(self):
        """
        Starts the next filter to resolve, if any.
        """
        if self.pending_filters:
            self.pending_filters[-1].filter(self.targets)

    def _start_next_selection(self):
        """
        Starts the next selection to resolve, if any.
        """
        if self.selections:
            self.selections[-1].resolve()
