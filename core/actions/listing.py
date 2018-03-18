action_listing = set()
action_mapping = {}


def register(action):
    action_mapping[action.id] = action


def get_by_id(action_id):
    return action_mapping.get(action_id)
