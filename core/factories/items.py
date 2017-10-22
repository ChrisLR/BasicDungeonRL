from core.gameobject import GameObject
from core import components
from core.util.colors import Colors
from core.displaypriority import DisplayPriority


class ItemFactory(object):
    @classmethod
    def create_new(cls, item_type):
        new = GameObject(blocking=False, name=item_type.name)
        if hasattr(item_type, 'ammunition_type') and item_type.ammunition_type \
                or hasattr(item_type, 'ammunition_damage') and item_type.ammunition_damage:
            new.register_component(components.Ammunition(item_type.ammunition_type, item_type.ammunition_damage))

        if hasattr(item_type, 'armor_class') and item_type.armor_class:
            new.register_component(components.Armor(item_type.armor_class, item_type.armor_type))

        if hasattr(item_type, 'container_type') and item_type.container_type:
            new.register_component(components.Container(
                container_type=getattr(item_type, 'container_type', None),
                containable_items=getattr(item_type, 'containable_items', None),
                max_quantity=getattr(item_type, 'max_quantity', None),
                volume_limit=getattr(item_type, 'volume_limit', None),
                weight_limit=getattr(item_type, 'weight_limit', None),
            ))

        if hasattr(item_type, 'price') and item_type.price:
            new.register_component(components.Sellable(item_type.price))

        if hasattr(item_type, 'size') and item_type.size:
            new.register_component(components.Size(item_type.size))

        if hasattr(item_type, 'wear_locations') and item_type.wear_locations:
            new.register_component(components.Wearable(item_type.wear_locations))

        if hasattr(item_type, 'weight') and item_type.weight:
            new.register_component(components.Weight(item_type.weight))

        new.register_component(components.Location())
        new.register_component(components.Display(
            Colors.GRAY, Colors.BLACK, item_type.name[0], DisplayPriority.Item))


        return new
