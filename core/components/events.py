from core.components.base import Component
from core.events import event_listing


class Events(Component):
    NAME = "events"
    __slots__ = ["mapping"]

    def __init__(self):
        super().__init__()
        self.mapping = {}
        self.initialize_event_types()

    def initialize_event_types(self):
        for event in event_listing:
            self.mapping[event] = []

    def register_listener(self, event_type, listener, func):
        self.mapping[event_type].append((listener, func))

    def unregister_listener(self, event_type, listener):
        self.mapping[event_type].remove(listener)

    def transmit(self, event):
        event_type = type(event)
        responders = self.mapping.get(event_type)
        for _, func in responders:
            func(event)

    def copy(self):
        return Events()
