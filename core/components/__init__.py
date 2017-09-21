from core.components.base import Component
from core.components.stats import CharacterStats
from core.components.character_class import CharacterClass
from core.components.equipment import Equipment
from core.components.experience import Experience
from core.components.money import Money
from core.components.race import Race
from core.components.restrictions import Restrictions

component_names = {
    CharacterClass.NAME,
    CharacterStats.NAME,
    Equipment.NAME,
    Experience.NAME,
    Money.NAME,
    Race.NAME,
    Restrictions.NAME
}
