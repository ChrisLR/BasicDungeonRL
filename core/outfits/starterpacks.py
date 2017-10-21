from bflib import items
from bflib.characters import classes
from core.outfits.base import Outfit


class BasicPack(Outfit):
    name = "Basic Pack"
    inventory_items = [
        items.Backpack,
        (6, items.Torch),
        items.TinderboxFlintAndSteel,
        items.Waterskin,
        items.WinterBlanket,
        items.Rations,
        items.LargeSack,
        (2, items.SmallSack),
    ]
    coins = items.coins.Gold(60)

    @classmethod
    def check_if_applicable(cls, game_object):
        return True


class FighterPack1(Outfit):
    name = "Fighter Pack 1"
    worn_items = [
        items.ChainMail,
    ]
    wielded_items = [
        items.MediumShield,
        items.Longsword,
    ]

    @classmethod
    def check_if_applicable(cls, game_object):
        character_class = game_object.character_class
        if character_class and character_class.contains(classes.Fighter):
            return True


class FighterPack2(Outfit):
    name = "Fighter Pack 2"
    worn_items = [
        items.ChainMail,
    ]
    wielded_items = [
        items.Polearm,
    ]

    @classmethod
    def check_if_applicable(cls, game_object):
        character_class = game_object.character_class
        if character_class and character_class.contains(classes.Fighter):
            return True


class FighterPack3(Outfit):
    name = "Fighter Pack 3"
    worn_items = [
        items.LeatherArmor,
        items.Quiver,
    ]
    wielded_items = [
        items.Longsword,
        items.Shortbow,
    ]
    inventory_items = [
        (30, items.ShortbowArrow)
    ]

    @classmethod
    def check_if_applicable(cls, game_object):
        character_class = game_object.character_class
        if character_class and character_class.contains(classes.Fighter):
            return True
