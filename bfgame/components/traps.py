from bfgame.components.base import Component
from core import events
from core.tiles.base import Floor


class Trap(Component):
    NAME = "trap"
    __slots__ = ["core_trap"]

    def __init__(self, core_trap):
        super().__init__()
        self.core_trap = core_trap
        self.triggers = []
        self.failed_attempts = {}

    @property
    def name(self):
        return self.core_trap.base_trap.name

    def add_failed_attempt(self, character, level):
        """ Attempts to remove can only be made once per level. """
        self.failed_attempts[character] = level

    def has_failed(self, character):
        attempt = self.failed_attempts.get(character)
        if attempt is None:
            return False

        if character.experience.level == attempt:
            return True

        return False

    def on_register(self, host):
        super().on_register(host)
        if host.container:
            self.triggers.append(events.Opened)

        if isinstance(host, Floor):
            self.triggers.append(events.WalkedOn)

        for event_type in self.triggers:
            host.events.register_listener(event_type, self, self.trigger)

    def on_unregister(self):
        for event_type in self.triggers:
            self.host.events.unregister_listener(event_type, self)
        super().on_unregister()

    def trigger(self, event):
        self.core_trap.trigger(self.host, event)
        self.host.unregister_component(self)

    def copy(self):
        return Trap(self.core_trap)
