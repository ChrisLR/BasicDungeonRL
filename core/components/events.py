from core.components.base import Component
from core.events import event_listing


class Events(Component):
    NAME = "events"
    __slots__ = ["mapping"]

    def __init__(self):
        super().__init__()
        self.mapping = {}
        self.initialize_event_types()
        self.funcs = {}

    def initialize_event_types(self):
        for event in event_listing:
            self.mapping[event] = set()

    def register_listener(self, event_type, listener, func):
        self.mapping[event_type].add(listener)
        self.funcs[listener] = func

    def unregister_listener(self, event_type, listener):
        event_type_listeners = self.mapping[event_type]
        if listener in event_type_listeners:
            self.mapping[event_type].remove(listener)
            del self.funcs[listener]

    def transmit(self, event):
        event_type = type(event)
        responders = list(self.mapping.get(event_type))
        for responder in responders:
            func = self.funcs.get(responder)
            func(event)

    def copy(self):
        return Events()
