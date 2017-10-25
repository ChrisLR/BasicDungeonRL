from bflib import units
from bflib.items import coins
from bflib.items.tools.base import ClimbingTool, Tool


class GrapplingHook(Tool):
    name = "Grappling Hook"

    price = coins.Gold(2)
    weight = units.Pound(4)


class IronSpike(Tool):
    name = "Iron Spike"

    price = coins.Copper(8)
    weight = units.Pound(0.1)


class Ladder(ClimbingTool):
    name = "Ladder"

    height = units.Feet(10)
    price = coins.Gold(1)
    weight = units.Pound(20)


class HempRope(ClimbingTool):
    name = "Hemp Rope"

    height = units.Feet(50)
    price = coins.Gold(1)
    weight = units.Pound(5)


class HolySymbol(Tool):
    name = "Holy Symbol"

    price = coins.Gold(25)
    weight = units.Pound(0.1)


class Key(Tool):
    name = "Key"

    price = coins.Silver(1)
    weight = units.Pound(0.1)


class Manacles(Tool):
    name = "Manacles"

    price = coins.Gold(6)
    weight = units.Pound(4)


class Padlock(Tool):
    name = "Padlock"

    price = coins.Gold(12)
    weight = units.Pound(4)


class SilkRope(ClimbingTool):
    name = "Silk Rope"

    height = units.Feet(50)
    price = coins.Gold(10)
    weight = units.Pound(2)


class ThievesPickAndTools(Tool):
    name = "Thieves Pick and Tools"

    price = coins.Gold(25)
    weight = units.Pound(1)


class TinderboxFlintAndSteel(Tool):
    name = "Tinderbox, flint and steel"

    price = coins.Gold(3)
    weight = units.Pound(1)


class Whetstone(Tool):
    name = "Whetstone"

    price = coins.Gold(1)
    weight = units.Pound(1)


class Whistle(Tool):
    name = "Whistle"

    price = coins.Gold(1)
    weight = units.Pound(0)
