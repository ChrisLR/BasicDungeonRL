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


def test_equipment_copy(sample_equipment):
    new_copy = sample_equipment.copy()

    assert new_copy is not sample_equipment
    for attr in sample_equipment.__dict__.keys():
        assert getattr(sample_equipment, attr) == getattr(new_copy, attr)


def test_equipment_wear(sample_equipment):
    built_item = ItemFactory.create_new(items.LeatherArmor)
    sample_equipment.wear(built_item)

    assert built_item in sample_equipment.get_worn_items()


def test_equipment_wield(self, item):
    pass


def test_equipment_remove_worn_item(self, item):
    pass

def test_equipment_remove_wielded_item(self, item):
    pass





@pytest.mark.xfail()
def test_equipment_get_total_armor_class(self):
    pass


def test_equipment_get_all_items(self):
    pass


def test_equipment_get_worn_items(self):
    pass


def test_equipment_get_load_of_worn_items(self):
    pass


def test_equipment_get_wielded_items(self):
    pass
