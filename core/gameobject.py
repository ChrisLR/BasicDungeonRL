from core.components.query import Query


class GameObject(object):
    __slots__ = ["_blocking", "components", "flags", "properties", "name"]

    def __init__(self, blocking=False, name="", flags=None):
        self._blocking = blocking
        self.components = {}
        self.flags = flags if flags else set()
        self.properties = {}
        self.name = name
        self.register_component(Query())

    @property
    def blocking(self):
        return self._blocking

    @blocking.setter
    def blocking(self, value):
        self._blocking = value
        location = self.location
        if location:
            level = location.level
            coordinate = location.get_local_coords()
            if level:
                level.reset_walkable_for_coordinate(coordinate)

    def copy_to(self, new_game_object):
        for component in self.components.values():
            new_game_object.register_component(component.copy())

        return new_game_object

    def get_component(self, component_name):
        return self.components.get(component_name, None)

    def round_update(self):
        for component in self.components.values():
            component.round_update()

    def minute_update(self):
        for component in self.components.values():
            component.minute_update()

    def hours_update(self):
        for component in self.components.values():
            component.hours_update()

    def days_update(self):
        for component in self.components.values():
            component.days_update()

    def register_component(self, component):
        if component.NAME in self.components:
            self.unregister_component(component)

        self.components[component.NAME] = component
        component.on_register(self)
        if component.properties:
            self.properties.update(component.properties)

    def register_forward(self, component):
        """
        This registers another object's component but does not change the host.
        """
        if component.NAME in self.components:
            self.unregister_component(component)

        self.components[component.NAME] = component
        if component.properties:
            self.properties.update(component.properties)

    def unregister_component(self, component):
        if component.NAME in self.components:
            component.on_unregister()
            del self.components[component.NAME]

    def unregister_component_name(self, component_name):
        if component_name in self.components:
            self.components[component_name].on_unregister()
            del self.components[component_name]

    def __getattr__(self, item):
        component = self.get_component(item)
        if component:
            return component

        from core.components import component_names
        if item in component_names:
            return NoneVoid()

        raise AttributeError()


class NoneVoid(object):
    """
    This class's only purpose is to Falsify any other calls make to get attributes from it.
    It allows us to duck type into components a little easier.
    """
    def __getattr__(self, item):
        return None

    def __bool__(self):
        return False
