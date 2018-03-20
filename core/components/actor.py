from core.components.base import Component
from core import actions


class Actor(Component):
    NAME = "actor"

    def __init__(self):
        super().__init__()
        self.action_stack = None

    def can_execute(self, action_id, target_selection=None):
        action = actions.listing.get_by_id(action_id)
        return action.can_execute(self.host, target_selection)

    def execute(self, action_id, target_selection=None):
        action = actions.listing.get_by_id(action_id)
        return action.execute(self.host, target_selection)

    def copy(self):
        return Actor()
