import pytest
from core import components
from bflib import items
from bflib.keywords.items import WearLocation, WieldLocation
from core.factories.items import ItemFactory


@pytest.fixture
def sample_equipment():
    wear_locations = WearLocation.__members__.values()
    wield_locations = WieldLocation.__members__.values()
    return components.Equipment(wear_locations=wear_locations, wield_locations=wield_locations)


# noinspection PyShadowingNames
def test_equipment_copy(sample_equipment):
    new_copy = sample_equipment.copy()

    assert new_copy is not sample_equipment
    for attr in sample_equipment.__dict__.keys():
        assert getattr(sample_equipment, attr) == getattr(new_copy, attr)


# noinspection PyShadowingNames
def test_equipment_wear(sample_equipment):
    built_item = ItemFactory.create_new(items.LeatherArmor)
    sample_equipment.wear(built_item)

    assert built_item in sample_equipment.get_worn_items()


# noinspection PyShadowingNames
def test_equipment_wield(sample_equipment):
    built_item = ItemFactory.create_new(items.Longsword)
    sample_equipment.wield(built_item)

    assert built_item in sample_equipment.get_wielded_items()


# noinspection PyShadowingNames
def test_equipment_remove_worn_item(sample_equipment):
    built_item = ItemFactory.create_new(items.LeatherArmor)
    sample_equipment.wear(built_item)
    sample_equipment.remove(built_item)

    assert built_item not in sample_equipment.get_worn_items()


# noinspection PyShadowingNames
def test_equipment_remove_wielded_item(sample_equipment):
    built_item = ItemFactory.create_new(items.Longsword)
    sample_equipment.wield(built_item)
    sample_equipment.remove(built_item)

    assert built_item not in sample_equipment.get_wielded_items()


# noinspection PyShadowingNames
def test_get_melee_total_armor_class(sample_equipment):
    sword_item = ItemFactory.create_new(items.Shortsword)
    shield_item = ItemFactory.create_new(items.MediumShield)
    armor_item = ItemFactory.create_new(items.LeatherArmor)
    sample_equipment.wield(sword_item)
    sample_equipment.wield(shield_item)
    sample_equipment.wear(armor_item)

    total_ac = shield_item.shield.armor_class_melee + armor_item.armor.armor_class
    assert total_ac == sample_equipment.get_melee_total_armor_class()


# noinspection PyShadowingNames
def test_get_ranged_total_armor_class(sample_equipment):
    sword_item = ItemFactory.create_new(items.Shortsword)
    shield_item = ItemFactory.create_new(items.MediumShield)
    armor_item = ItemFactory.create_new(items.LeatherArmor)
    sample_equipment.wield(sword_item)
    sample_equipment.wield(shield_item)
    sample_equipment.wear(armor_item)

    total_ac = shield_item.shield.armor_class_missile + armor_item.armor.armor_class
    assert total_ac == sample_equipment.get_ranged_total_armor_class()


# noinspection PyShadowingNames
def test_equipment_get_all_items(sample_equipment):
    wielded_built_item = ItemFactory.create_new(items.Longsword)
    worn_built_item = ItemFactory.create_new(items.LeatherArmor)
    sample_equipment.wield(wielded_built_item)
    sample_equipment.wear(worn_built_item)

    all_items = sample_equipment.get_all_items()

    assert wielded_built_item in all_items
    assert worn_built_item in all_items


# noinspection PyShadowingNames
def test_equipment_get_worn_items(sample_equipment):
    worn_built_item = ItemFactory.create_new(items.LeatherArmor)
    sample_equipment.worn_items = {WearLocation.Torso: worn_built_item}

    assert worn_built_item in sample_equipment.get_worn_items()


# noinspection PyShadowingNames
def test_equipment_get_wielded_items(sample_equipment):
    wielded_built_item = ItemFactory.create_new(items.Longsword)
    sample_equipment.wielded_items = {WieldLocation.LeftHand: wielded_built_item}

    assert wielded_built_item in sample_equipment.get_wielded_items()


# noinspection PyShadowingNames
def test_equipment_get_load_of_worn_items(sample_equipment):
    armor_built_item = ItemFactory.create_new(items.LeatherArmor)
    cloak_built_item = ItemFactory.create_new(items.Cloak)
    belt_built_item = ItemFactory.create_new(items.BeltPouch)
    sample_equipment.worn_items = {
        WearLocation.Torso: armor_built_item,
        WearLocation.Back: cloak_built_item,
        WearLocation.Waist: belt_built_item,
    }
    total_weight = armor_built_item.weight.score + cloak_built_item.weight.score + belt_built_item.weight.score

    assert total_weight == sample_equipment.get_load_of_worn_items()
