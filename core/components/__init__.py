from core.components.ai import AI
from core.components.ammunition import Ammunition
from core.components.armor import Armor
from core.components.alliance import Alliance
from core.components.base import Component
from core.components.body import Body
from core.components.character_class import CharacterClass
from core.components.combat import Combat
from core.components.consumable import Consumable
from core.components.container import Container
from core.components.contained import Contained
from core.components.corpse import Corpse
from core.components.display import Display
from core.components.effects import Effects
from core.components.equipment import Equipment
from core.components.events import Events
from core.components.experience import Experience
from core.components.gender import Gender
from core.components.health import Health
from core.components.inventory import Inventory
from core.components.light import Light
from core.components.liquidcontainer import LiquidContainer
from core.components.location import Location
from core.components.lock import Lock
from core.components.melee import Melee
from core.components.money import Money
from core.components.monster import Monster
from core.components.morale import Morale
from core.components.movement import Movement
from core.components.openable import Openable
from core.components.player import Player
from core.components.race import Race
from core.components.ranged import Ranged
from core.components.restrictions import Restrictions
from core.components.savingthrows import SavingThrows
from core.components.valuable import Valuable
from core.components.shield import Shield
from core.components.skills import Skills
from core.components.size import Size
from core.components.spawninfo import SpawnInfo
from core.components.specialcontainer import SpecialContainer
from core.components.stats import CharacterStats
from core.components.traps import Trap
from core.components.wearable import Wearable
from core.components.weight import Weight
from core.components.vision import Vision, SimpleVision

component_names = {
    AI.NAME,
    Alliance.NAME,
    Ammunition.NAME,
    Armor.NAME,
    Body.NAME,
    CharacterClass.NAME,
    CharacterStats.NAME,
    Combat.NAME,
    Consumable.NAME,
    Container.NAME,
    Contained.NAME,
    Corpse.NAME,
    Display.NAME,
    Effects.NAME,
    Equipment.NAME,
    Events.NAME,
    Experience.NAME,
    Gender.NAME,
    Health.NAME,
    Location.NAME,
    Lock.NAME,
    Light.NAME,
    LiquidContainer.NAME,
    Inventory.NAME,
    Melee.NAME,
    Money.NAME,
    Monster.NAME,
    Morale.NAME,
    Movement.NAME,
    Openable.NAME,
    Player.NAME,
    Race.NAME,
    Ranged.NAME,
    Restrictions.NAME,
    SavingThrows.NAME,
    Skills.NAME,
    Valuable.NAME,
    Shield.NAME,
    Size.NAME,
    SpawnInfo.NAME,
    SpecialContainer.NAME,
    Trap.NAME,
    Vision.NAME,
    SimpleVision.NAME,
    Wearable.NAME,
    Weight.NAME,
}
