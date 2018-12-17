class Component(object):
    """Base class for components"""
    NAME = "base_component"

    def __init__(self):
        self.host = None
        self.properties = {}

    def on_register(self, host):
        self.host = host

    def on_unregister(self):
        self.host = None

    def round_update(self):
        pass

    def minute_update(self):
        pass

    def hours_update(self):
        pass

    def days_update(self):
        pass

    def handle_message(self, message):
        pass
