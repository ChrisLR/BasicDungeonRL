class ActionStack(object):
    """
    Every action executed by the player will be added to this stack.
    Every selection needed by this action will be stacked and filtered.
    """
    def __init__(self, game_object, update_turn_callback=None):
        self.game_object = game_object
        self.action_resolutions = []
        self.update_turn_callback = update_turn_callback

    def add_action_to_stack(self, action):
        if action.target_selection_types:
            self.action_resolutions.append(ActionResolution(action, self.game_object))
        else:
            self._start_action(ActionResolution(action, self.game_object))

    def update(self):
        if not self.action_resolutions:
            return

        current_resolution = self.action_resolutions[-1]
        current_resolution.update()
        if current_resolution.finished_selection:
            if current_resolution.finished_filter:
                self._start_action(current_resolution)
                self.action_resolutions.remove(current_resolution)
                if not self.action_resolutions:
                    self.update_turn_callback()

    @staticmethod
    def _get_current_resolution(stack):
        return stack[-1].resolution

    @staticmethod
    def _start_next_resolution(stack):
        last_resolution = stack.pop(-1).resolution
        if stack:
            stack[-1].resolve(last_resolution)
            return True
        return False

    @staticmethod
    def _start_action(action_resolution):
        if action_resolution.can_execute_action:
            action_resolution.execute_action()


class ActionResolution(object):
    __slots__ = ["action", "executor", "selections", "pending_filters", "targets"]

    def __init__(self, action, executor):
        self.action = action
        self.executor = executor
        self.targets = []
        if action.target_filters:
            self.pending_filters = [target_filter() for target_filter in action.target_filters]
        else:
            self.pending_filters = None

        if action.target_selection_types:
            self.selections = [selection(executor) for selection in action.target_selection_types]
            self.start_next_selection()
        else:
            self.selections = None

    @property
    def can_execute_action(self):
        if self.action.can_execute(self.executor, self.targets):
            return True
        return False

    def execute_action(self):
        self.action.execute(self.executor, self.targets)

    @property
    def finished_selection(self):
        return not self.selections

    @property
    def finished_filter(self):
        return not self.pending_filters

    def update_filter(self):
        current_filter = self.pending_filters[-1]
        if current_filter.resolution:
            self.targets = current_filter.resolution
            self.pending_filters.pop(-1)
            self.start_next_filter()

    def start_next_filter(self):
        self.pending_filters[-1].filter(self.targets)

    def start_next_selection(self):
        if self.selections:
            self.selections[-1].resolve()

    def update(self):
        if self.selections:
            resolution = self.selections[-1].resolution
            if resolution:
                self.targets.extend(resolution)
                self.selections.pop(-1)
                self.start_next_selection()
        else:
            if self.pending_filters:
                self.update_filter()
