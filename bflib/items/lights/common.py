from bflib import dice, units
from bflib.items import coins, listing
from bflib.items.lights.base import LightItem
from bflib.items.weapons.throwing.common import OilFlask
from bflib.shapes import Shape


@listing.register_item
class Lantern(LightItem):
    name = "Lantern"

    bright_light_radius = units.Feet(30)
    dim_light_radius = units.Feet(20)
    fuel = OilFlask
    fuel_duration = units.GameTurn(18)
    last_life_dice = dice.D6(1)
    light_shape = Shape.Circle
    price = coins.Gold(5)
    weight = units.Pound(2)


@listing.register_item
class BullseyeLantern(Lantern):
    name = "Bullseye Lantern"

    light_shape = Shape.Cone
    price = coins.Gold(14)
    weight = units.Pound(3)


@listing.register_item
class Candle(LightItem):
    name = "Torch"

    bright_light_radius = units.Feet(5)
    dim_light_radius = units.Feet(5)
    fuel = None
    fuel_duration = units.GameTurn(4)
    last_life_dice = dice.D4(1)
    light_shape = Shape.Circle
    price = coins.Copper(10)
    weight = units.Pound(0.1)


@listing.register_item
class HoodedLantern(Lantern):
    name = "Hooded Lantern"

    price = coins.Gold(8)
    weight = units.Pound(2)


@listing.register_item
class Torch(LightItem):
    name = "Torch"

    bright_light_radius = units.Feet(30)
    dim_light_radius = units.Feet(20)
    fuel = None
    fuel_duration = units.GameTurn(4)
    last_life_dice = dice.D4(1)
    light_shape = Shape.Circle
    price = coins.Silver(1)
    weight = units.Pound(0.2)
