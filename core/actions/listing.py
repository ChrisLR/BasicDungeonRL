action_listing = set()
action_mapping = {}


def register(action):
    action_mapping[action.name] = action


def get_by_id(action_name):
    return action_mapping.get(action_name)
