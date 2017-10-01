from core.sex import Sex
from core.game.manager import game


def is_player(game_object):
    if game.game_context.player == game_object:
        return True
    return False


def his_her_it(value):
    if is_player(value):
        return "your"

    if hasattr(value, 'sex'):
        if value.sex == Sex.Male:
            return "his"
        if value.sex == Sex.Female:
            return "her"
    return "its"


def him_her_it(value):
    if is_player(value):
        return "you"

    if hasattr(value, 'sex'):
        if value.sex == Sex.Male:
            return "him"
        if value.sex == Sex.Female:
            return "her"
    return "its"


def he_her_it(value):
    if is_player(value):
        return "you"

    if hasattr(value, 'sex'):
        if value.sex == Sex.Male:
            return "he"
        if value.sex == Sex.Female:
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
