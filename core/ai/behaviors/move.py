from core.ai.behaviors.base import Behavior
from core.ai.pathing import ComputedPath
from core.actions.move import Walk
from core import direction


class Move(Behavior):
    def __init__(self, host, target_coordinates, simple=True):
        super().__init__(host)
        self.target_coordinates = target_coordinates
        self.computed_path = ComputedPath(host)
        self.simple = simple
        if not self.simple:
            self.computed_path.calculate(target_coordinates)

    def adjust_target_coordinates(self, new_coordinates):
        if new_coordinates != self.target_coordinates:
            self.target_coordinates = new_coordinates
            if not self.simple:
                self.computed_path.calculate(new_coordinates)

    def get_action(self):
        hx, hy = self.host.location.get_local_coords()
        if not self.simple:
            next_step = self.computed_path.next()
        else:
            tx, ty = self.target_coordinates
            x, y = 0, 0
            if tx > hx:
                x += 1
            elif tx < hx:
                x -= 1

            if ty > hy:
                y += 1
            elif ty < hy:
                y -= 1

            next_step = (x, y)

        if not next_step:
            return None

        for enum, coord in direction.move_direction_mapping.items():
            if coord == next_step:
                return Walk.from_direction(enum)
