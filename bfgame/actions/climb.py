from bfgame.actions.base import Action
from core.direction import Direction


class Climb(Action):
    name = "climb"
    direction = None

    def __init__(self, game):
        super().__init__(game)
        self.current_level = None
        self.level_exit = None

    def can_execute(self, character, target_selection=None):
        location = character.location
        self.current_level = location.level
        if self.current_level:
            tile = self.current_level.get_tile(location.get_local_coords())
            exit_component = tile.exit
            if not exit_component:
                return False

            level_exit = tile.exit.get_exit(self.direction)
            if level_exit:
                self.level_exit = level_exit
                return True

        return False

    def execute(self, character, target_selection=None):
        level_stub, exit_tile = self.level_exit
        new_level = level_stub.level
        self.current_level.remove_object(character)
        character.location.set_local_coords(exit_tile.location.get_local_coords())
        new_level.add_object(character)

        return True


class ClimbUp(Climb):
    name = "climb_up"
    direction = Direction.Up


class ClimbDown(Climb):
    name = "climb_down"
    direction = Direction.Down
