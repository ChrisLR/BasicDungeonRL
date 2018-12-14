import pytest

from bflib import skills
from bflib.characters import classes
from bflib.characters.abilityscores import AbilityScoreSet
from bfgame import components
from core.gameobject import GameObject


@pytest.fixture
def character():
    char_components = [
        components.CharacterStats(AbilityScoreSet.set_all(8, strength=14)),
        components.CharacterClass(classes.Fighter),
        components.Skills(),
    ]

    char = GameObject(None)

    for component in char_components:
        char.register_component(component)

    return char


def test_classed_skill_has_proper_cost(character):
    assert character.skills.get_increase_cost(skills.Jump) == 1


def test_unclassed_skill_has_proper_cost(character):
    assert character.skills.get_increase_cost(skills.ArcaneSpellcraft) == 3


def test_gets_proper_stat_bonus(character):
    assert character.skills.get_stat_bonus(skills.Jump) == 1
    assert character.skills.get_stat_bonus(skills.ArcaneSpellcraft) == -1


def test_increases_skill_value(character):
    character.skills.increase_skill(skills.Jump, 2)
    assert character.skills.get_base_skill_value(skills.Jump) == 2


def test_decreases_skill_value(character):
    character.skills.increase_skill(skills.Jump, 2)
    character.skills.decrease_skill(skills.Jump, 2)
    assert character.skills.get_base_skill_value(skills.Jump) == 0


def test_cant_decrease_skill_past_zero(character):
    character.skills.decrease_skill(skills.Jump, 2)
    assert character.skills.get_base_skill_value(skills.Jump) == 0


def test_gets_skill_value(character):
    character.skills.increase_skill(skills.Jump, 2)
    assert character.skills.get_skill_value(skills.Jump) == 2


def test_can_roll_values(character):
    character.skills.increase_skill(skills.Jump, 2)
    assert character.skills.roll_check(skills.Jump) >= 3
