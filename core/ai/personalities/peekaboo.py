from core.ai import behaviors
from core.ai.personalities.base import Personality
from services import echo


class Peekaboo(Personality):
    """
    Just a Test AI for the sneak.
    """
    @classmethod
    def get_behavior(cls, host, last_behavior, short_term_state):
        from core.game.manager import game
        level = host.location.level
        player = game.game_context.player
        if not level:
            return behaviors.Wait(host, 1)
        else:
            if host.vision.can_see_object(player):
                echo.system_echo("I See you!")
            else:
                echo.system_echo("You are hidden!")

        return behaviors.Wait(host, 1)

