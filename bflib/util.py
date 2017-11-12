def max_if(value1, value2):
    """
    Returns the largest value if it is not None
    """
    if value1 and value2:
        return max(value1, value2)
    elif value1 is not None and value2 is None:
        return value1
    elif value1 is None and value2 is not None:
        return value2

    return None


def merge_set_if_true(set_1, set_2):
    """
    Merges two sets if True
    :return: New Set
    """
    if set_1 and set_2:
        return set_1.from_merge(set_1, set_2)
    elif set_1 and not set_2:
        return set_1
    elif set_2 and not set_1:
        return set_2
    else:
        return None
