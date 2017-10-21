from bflib import items
from bflib.characters import classes
from core.outfits.base import Outfit


class BasicPack(Outfit):
    name = "Basic Pack"
    worn_items = [
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


class FighterPack(Outfit):
    name = "Fighter Pack I"
    worn_items = []
    wielded_items = []
    inventory_items = []
    coins = None

    @classmethod
    def check_if_applicable(cls, game_object):
        character_class = game_object.character_class
        if character_class and character_class.contains(classes.Fighter):
            return True
