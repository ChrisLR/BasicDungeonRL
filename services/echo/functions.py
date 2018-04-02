from core.gender import Gender


def is_player(game_object):
    if game_object.player:
        return True
    return False


def his_her_it(value):
    if is_player(value):
        return "your"

    if hasattr(value, 'gender'):
        if value.sex == Gender.Male:
            return "his"
        if value.sex == Gender.Female:
            return "her"
    return "its"


def him_her_it(value):
    if is_player(value):
        return "you"

    if hasattr(value, 'gender'):
        if value.sex == Gender.Male:
            return "him"
        if value.sex == Gender.Female:
            return "her"
    return "its"


def he_her_it(value):
    if is_player(value):
        return "you"

    if hasattr(value, 'gender'):
        if value.sex == Gender.Male:
            return "he"
        if value.sex == Gender.Female:
            return "her"
    return "it"


def name_or_you(value):
    if is_player(value):
        return "you"

    return value.name


def names_or_your(value):
    if is_player(value):
        return "your"

    return value.name + "'s"


def get_name_or_string(value):
    if not value:
        return ""
    if isinstance(value, str) or isinstance(value, int):
        return value
    else:
        return value.name
