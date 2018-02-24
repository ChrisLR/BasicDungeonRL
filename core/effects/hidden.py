from core import events, queries
from core.effects.base import Effect


class Hidden(Effect):
    name = "Hidden"

    def __init__(self, duration=None):
        super().__init__(duration, None, None)
        self._moved = False

    def on_start(self, game_object):
        game_object.query.register_responder(queries.Visibility, self, self._visibility_responder)
        game_object.events.register_listener(events.Moved, self, self._moved_listener)

    @property
    def finished(self):
        if self._moved:
            return True
        return super().finished

    def _moved_listener(self, event):
        # TODO This hack is bad
        from core.abilities.movesilently import MoveSilently

        if not MoveSilently.can_execute(event.actor) or not MoveSilently.execute(event.actor):
            self._moved = True

    def _visibility_responder(self, query):
        query.respond(type(self))

    def on_finish(self, game_object):
        game_object.query.unregister_responder(queries.Visibility, self)
        game_object.events.unregister_listener(events.Moved, self)
