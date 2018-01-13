import random


def get_unoccupied_position(level, origin_x, origin_y, width, height):
    tries = (origin_x * width) + (origin_y * height)
    while tries:
        tries -= 1
        x = random.randint(1, width) + origin_x
        y = random.randint(1, height) + origin_y
        coordinate = x, y
        tile = level.get_tile(coordinate)
        if not tile or tile.blocking:
            continue

        blocking_objects = [
            game_object for game_object
            in level.get_objects_by_coordinates(coordinate)
            if game_object.blocking]

        if blocking_objects:
            continue

        return coordinate