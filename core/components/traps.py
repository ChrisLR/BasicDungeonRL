from core.components.base import Component
from core import events
from core.tiles.floors import Floor


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
