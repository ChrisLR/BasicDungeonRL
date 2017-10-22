from core.gameobject import GameObject
from core import components
from core.util.colors import Colors
from core.displaypriority import DisplayPriority


class ItemFactory(object):
    @classmethod
    def create_new(cls, item_type):
        new = GameObject(blocking=False, name=item_type.name)
        new.register_component(components.Properties(
            wear_locations=item_type.wear_locations
        ))
        new.register_component(components.Location())
        new.register_component(components.Display(Colors.GRAY,
                                                  Colors.BLACK,
                                                  item_type.name[0],
                                                  DisplayPriority.Enemy))
        price = None
        size = Size.Medium
        wear_locations = tuple()
        weight = units.Pound

        return new
