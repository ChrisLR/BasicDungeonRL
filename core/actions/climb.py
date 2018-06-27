from core.actions.base import Action
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
            level_exit = tile.exit.get_exit(self.direction)
            if level_exit:
                self.level_exit = level_exit
                return True

        return False

    def execute(self, character, target_selection=None):
        new_level, new_position = self.level_exit
        self.current_level.remove_object(character)
        character.location.set_local_coords(new_position)
        new_level.add_object(character)

        return True


class ClimbUp(Climb):
    name = "climb_up"
    direction = Direction.Up


class ClimbDown(Climb):
    name = "climb_down"
    direction = Direction.Down
