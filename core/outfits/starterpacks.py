from bflib import items
from bflib.characters import classes
from core.outfits.base import Outfit


class BasicPack(Outfit):
    name = "Basic Pack"
    worn_items = [
        items.Backpack,
    ]
    inventory_items = [
        (6, items.Torch),
        items.TinderboxFlintAndSteel,
        items.Waterskin,
        items.WinterBlanket,
        items.DryRations,
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


class MagicUserPack1(Outfit):
    name = "Magic User Pack 1"
    worn_items = [
    ]
    wielded_items = [
        items.WalkingStaff,
    ]
    inventory_items = [
        (2, items.Dagger),
        items.MagicScroll,
    ]

    @classmethod
    def check_if_applicable(cls, game_object):
        character_class = game_object.character_class
        if character_class and character_class.contains(classes.MagicUser):
            return True


class MagicUserPack2(Outfit):
    name = "Magic User Pack 2"
    worn_items = [
    ]
    wielded_items = [
        items.WalkingStaff,
    ]
    inventory_items = [
        (2, items.Dagger),
    ]
    coins = items.coins.Gold(50)

    @classmethod
    def check_if_applicable(cls, game_object):
        character_class = game_object.character_class
        if character_class and character_class.contains(classes.MagicUser):
            return True


class ClericPack1(Outfit):
    name = "Cleric Pack 1"
    worn_items = [
        items.LeatherArmor,
    ]
    wielded_items = [
        items.Mace,
        items.MediumShield,
    ]
    inventory_items = [
        items.HolySymbol,
        items.Vial,
    ]

    @classmethod
    def check_if_applicable(cls, game_object):
        character_class = game_object.character_class
        if character_class and character_class.contains(classes.Cleric):
            return True


class ClericPack2(Outfit):
    name = "Cleric Pack 2"
    worn_items = [
        items.LeatherArmor,
    ]
    wielded_items = [
        items.Maul,
    ]
    inventory_items = [
        items.Sling,
        (30, items.SlingBullet),
        items.HolySymbol,
        items.Vial,
    ]

    @classmethod
    def check_if_applicable(cls, game_object):
        character_class = game_object.character_class
        if character_class and character_class.contains(classes.Cleric):
            return True


class ThiefPack1(Outfit):
    name = "Thief Pack 1"
    worn_items = [
        items.LeatherArmor,
    ]
    wielded_items = [
        items.Shortsword,
    ]
    inventory_items = [
        (2, items.Dagger),
        items.SilkRope,
        items.ThievesPickAndTools,
    ]

    @classmethod
    def check_if_applicable(cls, game_object):
        character_class = game_object.character_class
        if character_class and character_class.contains(classes.Thief):
            return True
