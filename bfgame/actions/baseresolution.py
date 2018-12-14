from bfgame.actions.base import Action
from core.gameobject import GameObject
from services.selection import TargetSelectionChain


class ActionResolution(object):
    """
    An object tracking an action's target resolution.
    """
    __slots__ = [
        "action", "executor", "game", "pending_selections", "pending_filters",
        "target_selections", "pending_target_selections"
    ]

    def __init__(self, action, executor, target_selection, game):
        """
        Filters and Selections will be instantiated to be resolved.
        Result of which are stored in target_selection.targets list.

        :param action: The Action to execute
        :type action: Action
        :param executor: The Executor GameObject
        :type executor: GameObject
        :param target_selection: Associated TargetSelection
        """

        self.action = action
        self.executor = executor
        self.game = game
        self.pending_filters = None
        self.pending_selections = None
        self.target_selections = target_selection.copy() if target_selection is not None else None
        if target_selection is None:
            return

        if isinstance(target_selection, TargetSelectionChain):
            self.pending_target_selections = list(self.target_selections.target_selection_sets)
        else:
            self.pending_target_selections = [self.target_selections]
        self.start_next_target_selection()

    def start_next_target_selection(self):
        if not self.pending_target_selections:
            return

        next_selection = self.pending_target_selections[0]
        if next_selection.filters:
            self.pending_filters = [
                target_filter(self.game, self.executor)
                for target_filter in next_selection.filters
            ]
        else:
            self.pending_filters = None

        if next_selection.selections:
            self.pending_selections = [
                selection(self.game, self.executor, next_selection)
                for selection in next_selection.selections
            ]
            self._start_next_selection()
        else:
            self.pending_selections = None

    def update(self):
        """
        Updates the selection and filter resolutions.
        """
        if not self.pending_selections and not self.pending_filters and self.pending_target_selections:
            self.pending_target_selections.pop(0)
            if not self.pending_target_selections:
                return
            self.start_next_target_selection()

        current_selection = self.pending_target_selections[0]
        if self.pending_selections:
            resolution = self.pending_selections[0].resolution
            canceled = self.pending_selections[0].canceled
            if resolution or canceled:
                if resolution:
                    current_selection.targets.extend(resolution)
                self.pending_selections.pop(0)
                if self.pending_selections:
                    self._start_next_selection()
                else:
                    self._start_next_filter()
        else:
            if self.pending_filters:
                self._update_filter()

    def can_execute_action(self):
        """
        Checks if current action can be executed with resolved targets.
        """
        if self.action.can_execute(self.executor, self.target_selections):
            return True
        return False

    def execute_action(self):
        """
        Executes action with resolved targets.
        """
        self.action.execute(self.executor, self.target_selections)

    @property
    def finished_selection(self):
        """
        Determines if the selection phase is finished.
        :return: bool
        """
        return not self.pending_selections

    @property
    def finished_filter(self):
        """
        Determines if the filter phase is finished.
        :return: bool
        """
        return not self.pending_filters

    @property
    def finished(self):
        """
        Determines if all Target Selections are finished
        :return: bool
        """
        return not self.pending_target_selections and not self.pending_selections and not self.pending_filters

    def _update_filter(self):
        """
        Updates top of the stack filter resolution.
        """
        current_selection = self.pending_target_selections[0]
        current_filter = self.pending_filters[0]
        if current_filter.resolution:
            current_selection.targets = current_filter.resolution
            self.pending_filters.pop(0)
            self._start_next_filter()

    def _start_next_filter(self):
        """
        Starts the next filter to resolve, if any.
        """
        current_selection = self.pending_target_selections[0]
        if self.pending_filters:
            self.pending_filters[0].filter(current_selection.targets)

    def _start_next_selection(self):
        """
        Starts the next selection to resolve, if any.
        """
        if self.pending_selections:
            self.pending_selections[0].resolve()
