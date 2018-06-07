from math import ceil


def manhattan_distance_to(origin_coords, target_coords):
    ox, oy = origin_coords
    tx, ty = target_coords
    return abs(ox - tx) + abs(oy - ty)


def feet_to_tiles(feet_value):
    return ceil(feet_value / 5)
