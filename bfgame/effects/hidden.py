from bfgame import queries
from core import events
from core.effects.base import Effect


class Hidden(Effect):
    name = "Hidden"

    def __init__(self, actor, duration=None):
        super().__init__(duration, None, None)
        self.actor = actor
        self._moved = False

    def on_start(self, game_object):
        game_object.query.register_responder(queries.Visibility, self, self._visibility_responder)
        game_object.events.register_listener(events.Moved, self, self._moved_listener)
        game_object.events.register_listener(events.Attacking, self, self._attacking)

    @property
    def finished(self):
        if self._moved:
            self.actor.game.echo.see(
                actor=self.actor,
                actor_message="You come out of hiding!",
                observer_message="{} comes out of hiding!".format(self.actor.name)
            )
            return True
        return super().finished

    def _attacking(self, event):
        self._moved = True
        event.actor.game.echo.see(
            actor=event.actor,
            actor_message="You come out of hiding!",
            observer_message="{} comes out of hiding!".format(event.actor.name)
        )

    def _moved_listener(self, event):
        # TODO This hack is bad
        from bfgame.abilities.movesilently import MoveSilently
        move_silently = MoveSilently(event.actor.game)

        if not move_silently.can_execute(event.actor) or not move_silently.execute(event.actor):
            self._moved = True

    def _visibility_responder(self, query):
        query.respond(type(self))

    def on_finish(self, game_object):
        game_object.query.unregister_responder(queries.Visibility, self)
        game_object.events.unregister_listener(events.Moved, self)
        game_object.events.unregister_listener(events.Attacking, self)
