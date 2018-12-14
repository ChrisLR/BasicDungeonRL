from bfgame.outfits import starterpacks
from bfgame.outfits.base import Outfit
from bfgame.outfits.outfitter import OutfitterService


def test_get_starter_package(sample_player):
    package = OutfitterService.get_starter_package(sample_player)
    assert issubclass(package, Outfit)
    assert package.check_if_applicable(sample_player)


def test_get_base_package(sample_player):
    package = OutfitterService.get_base_package(sample_player)
    assert issubclass(package, Outfit)
    assert package.check_if_applicable(sample_player)


def test_outfit_starting_player(sample_player, monkeypatch):
    monkeypatch.setattr(OutfitterService, 'get_base_package', lambda _: starterpacks.BasicPack)
    monkeypatch.setattr(OutfitterService, 'get_starter_package', lambda _: starterpacks.FighterPack1)
    OutfitterService.outfit_starting_player(sample_player)

    wielded_item_names = [item.name for item in sample_player.equipment.get_wielded_items()]
    worn_item_names = [item.name for item in sample_player.equipment.get_worn_items()]
    inventory_names = [item.name for item in sample_player.inventory.get_all_items()]

    expected_wield_count = len(starterpacks.FighterPack1.wielded_items) + len(starterpacks.BasicPack.wielded_items)
    expected_worn_count = len(starterpacks.FighterPack1.worn_items) + len(starterpacks.BasicPack.worn_items)
    expected_inv_count = len(starterpacks.FighterPack1.inventory_items) + len(starterpacks.BasicPack.inventory_items)

    assert expected_wield_count == len(wielded_item_names)
    assert expected_worn_count == len(worn_item_names)
    assert expected_inv_count == len(inventory_names)
    for item in starterpacks.FighterPack1.wielded_items:
        assert item.name in wielded_item_names

    for item in starterpacks.FighterPack1.worn_items:
        assert item.name in worn_item_names

    for item in starterpacks.FighterPack1.inventory_items:
        assert item.name in inventory_names

    monkeypatch.undo()
