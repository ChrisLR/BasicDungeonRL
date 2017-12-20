def manhattan_distance_to(origin_coords, target_coords):
    ox, oy = origin_coords
    tx, ty = target_coords
    return abs(ox - tx) + abs(oy - ty)
