from bflib.monsters import listing
from bflib.monsters.animals.bats import Bat, GiantBat
from bflib.monsters.animals.base import Animal


def test_get_monsters_by_type():
    monster_list = listing.get_monsters_by_type()[Bat]
    assert Bat in monster_list
    assert GiantBat in monster_list


def test_get_monsters_by_type_with_filter():
    monster_list = listing.get_monsters_by_type(Bat)
    assert Bat in monster_list
    assert GiantBat in monster_list


def test_get_monsters_by_type_with_generic_filter():
    monster_list = listing.get_monsters_by_type(Animal)
    assert Bat in monster_list
    assert GiantBat in monster_list
