from core.components.ammunition import Ammunition
from core.components.armor import Armor
from core.components.base import Component
from core.components.combat import Combat
from core.components.container import Container
from core.components.stats import CharacterStats
from core.components.character_class import CharacterClass
from core.components.display import Display
from core.components.equipment import Equipment
from core.components.experience import Experience
from core.components.health import Health
from core.components.location import Location
from core.components.light import Light
from core.components.inventory import Inventory
from core.components.melee import Melee
from core.components.money import Money
from core.components.monster import Monster
from core.components.morale import Morale
from core.components.movement import Movement
from core.components.race import Race
from core.components.restrictions import Restrictions
from core.components.savingthrows import SavingThrows
from core.components.sellable import Sellable
from core.components.shield import Shield
from core.components.size import Size
from core.components.spawninfo import SpawnInfo
from core.components.wearable import Wearable
from core.components.weight import Weight

component_names = {
    Ammunition.NAME,
    Armor.NAME,
    CharacterClass.NAME,
    CharacterStats.NAME,
    Combat.NAME,
    Container.NAME,
    Display.NAME,
    Equipment.NAME,
    Experience.NAME,
    Health.NAME,
    Location.NAME,
    Light.NAME,
    Inventory.NAME,
    Melee.NAME,
    Money.NAME,
    Monster.NAME,
    Morale.NAME,
    Movement.NAME,
    Race.NAME,
    Restrictions.NAME,
    SavingThrows.NAME,
    Sellable.NAME,
    Shield.NAME,
    Size.NAME,
    SpawnInfo.NAME,
    Wearable.NAME,
    Weight.NAME,
}
