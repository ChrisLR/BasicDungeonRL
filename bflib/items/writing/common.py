from bflib import units
from bflib.items import coins, listing
from bflib.items.writing.base import WritingItem
from bflib.sizes import Size


@listing.register_item
class Chalk(WritingItem):
    name = "Chalk"

    price = coins.Gold(2)
    size = Size.Small
    weight = units.Pound(0.1)


@listing.register_item
class InkJar(WritingItem):
    name = "Ink Jar"

    price = coins.Gold(8)
    size = Size.Small
    weight = units.Pound(0.5)


@listing.register_item
class Map(WritingItem):
    name = "Map"

    price = coins.Gold(1)
    size = Size.Small
    weight = units.Pound(0)


@listing.register_item
class Paper(WritingItem):
    name = "Paper"

    price = coins.Gold(1)
    size = Size.Small
    weight = units.Pound(0)


@listing.register_item
class Quill(WritingItem):
    name = "Quill"

    price = coins.Silver(1)
    size = Size.Small
    weight = units.Pound(0)


@listing.register_item
class Scroll(WritingItem):
    name = "Scroll"

    price = coins.Gold(1)
    size = Size.Small
    weight = units.Pound(0)
