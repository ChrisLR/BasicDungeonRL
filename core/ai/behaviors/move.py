from core.ai.behaviors.base import Behavior
from core.ai.pathing import ComputedPath
from core.actions.move import Walk
from core import direction


class Move(Behavior):
    def __init__(self, host, target_coordinates):
        super().__init__(host)
        self.target_coordinates = target_coordinates
        self.computed_path = ComputedPath(host)
        self.computed_path.calculate(target_coordinates)

    def execute(self):
        next_step = self.computed_path.next()
        if not next_step:
            return None

        for enum, coord in direction.move_direction_mapping.items():
            if coord == next_step:
                return Walk.from_direction(enum)
