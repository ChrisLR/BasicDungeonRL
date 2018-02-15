from core.components.base import Component
from core import events


class Trap(Component):
    NAME = "trap"
    __slots__ = ["core_trap"]

    def __init__(self, core_trap):
        super().__init__()
        self.core_trap = core_trap
        self.triggers = []

    def on_register(self, host):
        super().on_register(host)
        if host.container:
            self.triggers.append(events.Opened)

        for event_type in self.triggers:
            host.events.register_listener(event_type, self, self.trigger)

    def on_unregister(self):
        super().on_unregister()
        for event_type in self.triggers:
            self.host.events.unregister_listener(event_type, self)

    def trigger(self, event):
        self.core_trap.trigger(event)

    def copy(self):
        return Trap(self.core_trap)
