class ActionStack(object):
    """
    Every action executed by the player will be added to this stack.
    Every selection needed by this action will be stacked and filtered recursively.
    """
    def __init__(self, game_object):
        self.game_object = game_object
        self.actions = []

    def add_action_to_stack(self, action):
        self.actions.append((action, list()))

    def update(self):
        current_stack = self._get_current_stack(self.actions)
        if not current_stack:
            return

        resolution = self._get_current_resolution(current_stack)
        if not resolution:
            return

        if not self._start_next_resolution(current_stack):
            self._start_action(self.actions[-1], self.game_object, resolution)

    @staticmethod
    def _get_current_stack(actions):
        if actions:
            current_action, stack = actions[-1]

            return stack

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
    def _start_action(action, game_object, last_resolution):
        if action.can_execute(game_object, last_resolution):
            action.execute(game_object, last_resolution)
