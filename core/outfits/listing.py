outfit_listing = {}


def register(outfit):
    outfit_listing[outfit.name] = outfit
    return outfit


def get_by_name(outfit_name):
    return outfit_listing.get(outfit_name)
