from bflib import units
from bflib.items import coins, listing
from bflib.items.containers.base import Container
from bflib.keywords.items import WearLocation
from bflib.sizes import Size


@listing.register_item
class Backpack(Container):
    name = "Backpack"

    container_type = Container
    price = coins.Gold(4)
    size = Size.Medium
    volume_limit = units.CubicFeet(3)
    wear_locations = WearLocation.Back,
    weight = units.Pound(0.1)
    weight_limit = units.Pound(40)


@listing.register_item
class BeltPouch(Container):
    name = "Belt Pouch"

    container_type = Container
    price = coins.Gold(1)
    size = Size.Small
    volume_limit = units.CubicFeet(1)
    wear_locations = WearLocation.Belt,
    weight = units.Pound(0.1)
    weight_limit = units.Pound(10)


@listing.register_item
class Chest(Container):
    name = "Chest"

    container_type = Container
    price = coins.Gold(10)
    size = Size.Medium
    volume_limit = units.CubicFeet(8)
    wear_locations = None
    weight = units.Pound(10)
    weight_limit = units.Pound(80)


@listing.register_item
class LargeSack(Container):
    name = "Large Sack"

    container_type = Container
    price = coins.Gold(1)
    size = Size.Medium
    volume_limit = units.CubicFeet(4)
    weight = units.Pound(0.1)
    weight_limit = units.Pound(40)


@listing.register_item
class Saddlebags(Container):
    name = "Saddlebags"

    container_type = Container
    price = coins.Gold(4)
    size = Size.Small
    volume_limit = units.CubicFeet(1)
    weight = units.Pound(7)
    weight_limit = units.Pound(10)


@listing.register_item
class SmallBackpack(Container):
    name = "Small Backpack"

    container_type = Container
    price = coins.Gold(4)
    size = Size.Small
    volume_limit = units.CubicFeet(1.5)
    wear_locations = WearLocation.Back,
    weight = units.Pound(0.1)
    weight_limit = units.Pound(30)


@listing.register_item
class SmallSack(Container):
    name = "Small Sack"

    container_type = Container
    price = coins.Silver(5)
    size = Size.Small
    volume_limit = units.CubicFeet(2)
    weight = units.Pound(0.1)
    weight_limit = units.Pound(20)
