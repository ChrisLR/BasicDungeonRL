from bflib import dice
from bflib.items import coins
from bflib.items.armor.base import Armor
from bflib.items.gems.base import Gem
from bflib.items.jewelry.base import Jewelry
from bflib.items.potions.base import Potion
from bflib.items.weapons.base import Weapon
from bflib.items.writing.magical import MagicScroll
from bflib.treasuretypes import TreasureType


class RandomMagicItem(object):
    pass


class TreasureElement(object):
    __slots__ = ["amount", "extras", "treasure_value_type", "percent"]

    def __init__(self, percent, treasure_value_type, amount, *extras):
        """
        An Element of the Treasure Table
        :param percent: Change of being rolled.
        :param treasure_value_type: Coin Type or iterable of some type
        :param amount: Dice or fixed Int
        """
        self.amount = amount
        self.percent = percent
        self.treasure_value_type = treasure_value_type
        self.extras = extras


class TreasureRow(object):
    __slots__ = ["treasure_type", "elements"]

    def __init__(self, treasure_type, *elements):
        self.treasure_type = treasure_type
        self.elements = elements


class TreasureTable(object):
    rows = [
        TreasureRow(
            TreasureType.A,
            TreasureElement(50, coins.Copper, dice.D6(5)),
            TreasureElement(60, coins.Silver, dice.D6(5)),
            TreasureElement(40, coins.Electrum, dice.D4(5)),
            TreasureElement(70, coins.Gold, dice.D6(10)),
            TreasureElement(50, coins.Platinum, dice.D10(1)),
            TreasureElement(50, (Gem,), dice.D6(6)),
            TreasureElement(50, (Jewelry,), dice.D6(6)),
            TreasureElement(30, (RandomMagicItem,), 3)
        ),
        TreasureRow(
            TreasureType.B,
            TreasureElement(75, coins.Copper, dice.D10(5)),
            TreasureElement(50, coins.Silver, dice.D6(5)),
            TreasureElement(50, coins.Electrum, dice.D4(5)),
            TreasureElement(50, coins.Gold, dice.D6(3)),
            TreasureElement(25, Gem, dice.D6(1)),
            TreasureElement(25, Jewelry, dice.D6(1)),
            TreasureElement(10, (Armor, Weapon,), 1)
        ),
        TreasureRow(
            TreasureType.C,
            TreasureElement(60, coins.Copper, dice.D6(6)),
            TreasureElement(60, coins.Silver, dice.D4(5)),
            TreasureElement(30, coins.Electrum, dice.D6(2)),
            TreasureElement(25, Gem, dice.D4(1)),
            TreasureElement(25, Jewelry, dice.D4(1)),
            TreasureElement(15, (Armor, Weapon,), dice.D2(1))
        ),
        TreasureRow(
            TreasureType.D,
            TreasureElement(30, coins.Copper, dice.D6(4)),
            TreasureElement(45, coins.Silver, dice.D6(6)),
            TreasureElement(90, coins.Gold, dice.D8(5)),
            TreasureElement(30, Gem, dice.D8(1)),
            TreasureElement(30, Jewelry, dice.D8(1)),
            TreasureElement(20, RandomMagicItem, dice.D2(1), Potion)
        ),
        TreasureRow(
            TreasureType.E,
            TreasureElement(30, coins.Copper, dice.D8(2)),
            TreasureElement(60, coins.Silver, dice.D6(10)),
            TreasureElement(50, coins.Electrum, dice.D8(3)),
            TreasureElement(50, coins.Gold, dice.D10(4)),
            TreasureElement(10, Gem, dice.D10(1)),
            TreasureElement(10, Jewelry, dice.D10(1)),
            TreasureElement(30, RandomMagicItem, dice.D4(1), MagicScroll)
        ),
        TreasureRow(
            TreasureType.F,
            TreasureElement(40, coins.Silver, dice.D8(3)),
            TreasureElement(50, coins.Electrum, dice.D8(4)),
            TreasureElement(85, coins.Gold, dice.D10(6)),
            TreasureElement(70, coins.Platinum, dice.D8(2)),
            TreasureElement(20, Gem, dice.D12(2)),
            TreasureElement(10, Jewelry, dice.D12(1)),
            TreasureElement(35, RandomMagicItem, dice.D4(1), Potion, MagicScroll)
        ),
        TreasureRow(
            TreasureType.G,
            TreasureElement(90, coins.Gold, dice.D6(4, multiplier=10)),
            TreasureElement(75, coins.Platinum, dice.D8(5)),
            TreasureElement(25, Gem, dice.D6(3)),
            TreasureElement(25, Jewelry, dice.D10(1)),
            TreasureElement(50, RandomMagicItem, dice.D4(1), MagicScroll)
        ),
        TreasureRow(
            TreasureType.H,
            TreasureElement(75, coins.Copper, dice.D10(8)),
            TreasureElement(75, coins.Silver, dice.D10(6, multiplier=10)),
            TreasureElement(75, coins.Electrum, dice.D10(3, multiplier=10)),
            TreasureElement(75, coins.Gold, dice.D8(5, multiplier=10)),
            TreasureElement(75, coins.Platinum, dice.D8(9)),
            TreasureElement(50, Gem, dice.D100(1)),
            TreasureElement(50, Jewelry, dice.D4(10)),
            TreasureElement(20, RandomMagicItem, dice.D4(1), Potion, MagicScroll)
        ),
        TreasureRow(
            TreasureType.I,
            TreasureElement(80, coins.Platinum, dice.D10(3)),
            TreasureElement(50, Gem, dice.D6(2)),
            TreasureElement(50, Jewelry, dice.D6(2)),
            TreasureElement(15, RandomMagicItem, 1)
        ),
        TreasureRow(
            TreasureType.J,
            TreasureElement(45, coins.Copper, dice.D8(3)),
            TreasureElement(45, coins.Silver, dice.D8(1)),
        ),
        TreasureRow(
            TreasureType.K,
            TreasureElement(90, coins.Silver, dice.D10(2)),
            TreasureElement(35, coins.Electrum, dice.D8(1)),
        ),
        TreasureRow(
            TreasureType.L,
            TreasureElement(50, Gem, dice.D4(1)),
        ),
        TreasureRow(
            TreasureType.M,
            TreasureElement(90, coins.Gold, dice.D10(4)),
            TreasureElement(90, coins.Platinum, dice.D8(2, multiplier=10)),
            TreasureElement(55, Gem, dice.D4(5)),
            TreasureElement(45, Jewelry, dice.D6(2)),
        ),
        TreasureRow(
            TreasureType.N,
            TreasureElement(40, Potion, dice.D4(2)),
        ),
        TreasureRow(
            TreasureType.O,
            TreasureElement(50, MagicScroll, dice.D4(1)),
        ),
        TreasureRow(
            TreasureType.P,
            TreasureElement(100, coins.Copper, dice.D8(3)),
        ),
        TreasureRow(
            TreasureType.Q,
            TreasureElement(100, coins.Silver, dice.D6(3)),
        ),
        TreasureRow(
            TreasureType.R,
            TreasureElement(100, coins.Electrum, dice.D6(2)),
        ),
        TreasureRow(
            TreasureType.S,
            TreasureElement(100, coins.Gold, dice.D4(2)),
        ),
        TreasureRow(
            TreasureType.T,
            TreasureElement(100, coins.Platinum, dice.D6(1)),
        ),
        TreasureRow(
            TreasureType.U,
            TreasureElement(50, coins.Copper, dice.D20(1)),
            TreasureElement(50, coins.Silver, dice.D20(1)),
            TreasureElement(25, coins.Gold, dice.D20(1)),
            TreasureElement(5, Gem, dice.D4(1)),
            TreasureElement(5, Jewelry, dice.D4(1)),
            TreasureElement(2, RandomMagicItem, 1),
        ),
        TreasureRow(
            TreasureType.V,
            TreasureElement(25, coins.Silver, dice.D20(1)),
            TreasureElement(25, coins.Electrum, dice.D20(1)),
            TreasureElement(50, coins.Gold, dice.D20(1)),
            TreasureElement(25, coins.Platinum, dice.D20(1)),
            TreasureElement(10, Gem, dice.D4(1)),
            TreasureElement(10, Jewelry, dice.D4(1)),
            TreasureElement(5, RandomMagicItem, 1),
        ),

    ]
    inner_table = {row.treasure_type: row for row in rows}

    @classmethod
    def get_row(cls, treasure_type):
        """
        :type treasure_type: TreasureType
        :rtype: TreasureRow
        """
        return cls.inner_table.get(treasure_type)
