from core.effects.base import Effect
from services import echo


class Hidden(Effect):
    name = "Hidden"

    def __init__(self, duration):
        super().__init__(duration, None, None)

    def on_start(self, game_object):
        pass

    def _visibility_responder(self, query):
        query.respond({type(self): False})

    def on_finish(self, game_object):
        echo.see(
            actor=game_object,
            actor_message="You are no longer healing.",
            observer_message="{} is no longer healing.".format(game_object.name)
        )
