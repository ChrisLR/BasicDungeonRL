from bflib import items
from core.outfits.base import Outfit


def test_outfit_equip_worn_items(sample_player):
    Outfit._equip_worn_items([items.LeatherArmor], sample_player)
    assert items.LeatherArmor.name in [item.name for item in sample_player.equipment.get_worn_items()]


def test_outfit_equip_wielded_items(sample_player):
    Outfit._equip_wielded_items([items.Longsword], sample_player)
    assert items.LeatherArmor.name in [item.name for item in sample_player.equipment.get_wielded_items()]


def test_outfit_add_inventory_items(sample_player):
    Outfit._add_inventory_items([items.Torch], sample_player)
    assert items.Torch.name in [item.name for item in sample_player.equipment.get_wielded_items()]


def test_outfit_unpack_tuples():
    unpack_list = [(6, items.OilFlask), (2, items.Torch)]
    unpacked_listing = Outfit.unpack(unpack_list)

    assert len([item for item in unpacked_listing if item is items.OilFlask]) == 6
    assert len([item for item in unpacked_listing if item is items.Torch]) == 2


def test_outfit_singular_items():
    unpack_list = [items.OilFlask, items.Torch]
    unpacked_listing = Outfit.unpack(unpack_list)

    assert len(unpacked_listing) == 2
