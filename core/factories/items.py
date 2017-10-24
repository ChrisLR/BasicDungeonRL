from core.gameobject import GameObject
from core import components
from core.util.colors import Colors
from core.displaypriority import DisplayPriority


class ItemFactory(object):
    _item_components = [
        components.Weight,
        components.Wearable,
        components.Size,
        components.Ammunition,
        components.Armor,
        components.Container,
        components.Light,
        components.Inventory,
        components.Melee,
        components.Money,
        components.Sellable,
        components.Shield,
    ]

    @classmethod
    def create_new(cls, item_type):
        try:
            new = GameObject(blocking=False, name=item_type.name)
            for component in cls._item_components:
                if any(hasattr(item_type, slot) for slot in component.__slots__):
                    new.register_component(
                        component(**{slot: getattr(item_type, slot, None)
                                     for slot in component.__slots__}))

            new.register_component(components.Location())
            new.register_component(components.Display(
                Colors.GRAY, Colors.BLACK, item_type.name[0], DisplayPriority.Item))

        except Exception as exception:
            raise

        return new
