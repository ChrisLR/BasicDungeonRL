from core.ai.behaviors import Behavior
from core.ai.pathing import ComputedPath
from bfgame.actions.move import Walk
from core import direction


class Move(Behavior):
    def __init__(self, host, target_coordinates):
        super().__init__(host)
        self.target_coordinates = target_coordinates
        self.computed_path = ComputedPath(host)
        self.computed_path.calculate(target_coordinates)
        self.finished = False

    def adjust_target_coordinates(self, new_coordinates):
        if new_coordinates != self.target_coordinates:
            self.target_coordinates = new_coordinates
            self.computed_path.calculate(new_coordinates)

    def execute(self):
        next_step = self.computed_path.next()
        if not next_step:
            self.finished = True
            return

        move_action = None
        for enum, coord in direction.move_direction_mapping.items():
            if coord == next_step:
                move_action = Walk.from_direction(enum)(self.host.game)
                break

        if move_action:
            result = move_action.execute(self.host)
            if not result:
                self.computed_path.calculate(self.target_coordinates)
