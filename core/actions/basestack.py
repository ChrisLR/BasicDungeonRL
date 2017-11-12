from core.actions.base import Action
from core.actions.baseresolution import ActionResolution


class ActionStack(object):
    """
    An action stack keeping track of the action resolutions of a game object.
    """
    __slots__ = ["game_object", "action_resolutions", "update_turn_callback"]

    def __init__(self, game_object, update_turn_callback=None):
        """
        :param game_object: The executor game object
        :param update_turn_callback: The callback, if any, to update to next turn.
        """

        self.game_object = game_object
        self.action_resolutions = []
        self.update_turn_callback = update_turn_callback

    def add_action_to_stack(self, action):
        """
        This will add an action to the stack if it needs resolution
        or execute it straight away if it doesn't.

        :param action: The action to be executed.
        :type action: Action
        """

        if action.target_selection_types:
            self.action_resolutions.append(ActionResolution(action, self.game_object))
        else:
            self._start_action(ActionResolution(action, self.game_object))

    def update(self):
        """
        This will update the resolution on the top of the stack.
        Once the selections and filters are resolved it executes an action.
        """

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
    def _start_action(action_resolution):
        """
        Executes an action using the resolved targets.
        :param action_resolution: The ActionResolution to execute.
        :type action_resolution: ActionResolution
        """

        if action_resolution.can_execute_action:
            action_resolution.execute_action()
