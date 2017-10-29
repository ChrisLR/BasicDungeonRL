from bflib.items import listing
from bflib.items.weapons.melee.axes import Axe, GreatAxe
from bflib.items.weapons.melee.base import MeleeWeapon


def test_get_items_by_type():
    item_list = listing.get_items_by_type()[Axe]
    assert GreatAxe in item_list


def test_get_items_by_type_with_filter():
    item_list = listing.get_items_by_type(Axe)
    assert GreatAxe in item_list


def test_get_items_by_type_with_generic_filter():
    item_list = listing.get_items_by_type(MeleeWeapon)
    assert GreatAxe in item_list
