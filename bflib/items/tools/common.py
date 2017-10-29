from bflib import units
from bflib.items import coins, listing
from bflib.items.tools.base import ClimbingTool, Tool


@listing.register_item
class GrapplingHook(Tool):
    name = "Grappling Hook"

    price = coins.Gold(2)
    weight = units.Pound(4)


@listing.register_item
class IronSpike(Tool):
    name = "Iron Spike"

    price = coins.Copper(8)
    weight = units.Pound(0.1)


@listing.register_item
class Ladder(ClimbingTool):
    name = "Ladder"

    height = units.Feet(10)
    price = coins.Gold(1)
    weight = units.Pound(20)


@listing.register_item
class HempRope(ClimbingTool):
    name = "Hemp Rope"

    height = units.Feet(50)
    price = coins.Gold(1)
    weight = units.Pound(5)


@listing.register_item
class HolySymbol(Tool):
    name = "Holy Symbol"

    price = coins.Gold(25)
    weight = units.Pound(0.1)


@listing.register_item
class Key(Tool):
    name = "Key"

    price = coins.Silver(1)
    weight = units.Pound(0.1)


@listing.register_item
class Manacles(Tool):
    name = "Manacles"

    price = coins.Gold(6)
    weight = units.Pound(4)


@listing.register_item
class Padlock(Tool):
    name = "Padlock"

    price = coins.Gold(12)
    weight = units.Pound(4)


@listing.register_item
class SilkRope(ClimbingTool):
    name = "Silk Rope"

    height = units.Feet(50)
    price = coins.Gold(10)
    weight = units.Pound(2)


@listing.register_item
class ThievesPickAndTools(Tool):
    name = "Thieves Pick and Tools"

    price = coins.Gold(25)
    weight = units.Pound(1)


@listing.register_item
class TinderboxFlintAndSteel(Tool):
    name = "Tinderbox, flint and steel"

    price = coins.Gold(3)
    weight = units.Pound(1)


@listing.register_item
class Whetstone(Tool):
    name = "Whetstone"

    price = coins.Gold(1)
    weight = units.Pound(1)


@listing.register_item
class Whistle(Tool):
    name = "Whistle"

    price = coins.Gold(1)
    weight = units.Pound(0)
