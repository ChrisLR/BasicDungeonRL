from bfgame.components.ai import AI
from bfgame.components.ammunition import Ammunition
from bfgame.components.armor import Armor
from bfgame.components.alliance import Alliance
from bfgame.components.base import Component
from bfgame.components.body import Body
from bfgame.components.character_class import CharacterClass
from bfgame.components.combat import Combat
from bfgame.components.consumable import Consumable
from bfgame.components.container import Container
from bfgame.components.contained import Contained
from bfgame.components.corpse import Corpse
from bfgame.components.display import Display
from bfgame.components.effects import Effects
from bfgame.components.equipment import Equipment
from bfgame.components.events import Events
from bfgame.components.exit import Exit
from bfgame.components.experience import Experience
from bfgame.components.gender import Gender
from bfgame.components.health import Health
from bfgame.components.inventory import Inventory
from bfgame.components.light import Light
from bfgame.components.liquidcontainer import LiquidContainer
from bfgame.components.location import Location, TileLocation
from bfgame.components.lock import Lock
from bfgame.components.melee import Melee
from bfgame.components.money import Money
from bfgame.components.monster import Monster
from bfgame.components.morale import Morale
from bfgame.components.movement import Movement
from bfgame.components.openable import Openable
from bfgame.components.player import Player
from bfgame.components.race import Race
from bfgame.components.ranged import Ranged
from bfgame.components.restrictions import Restrictions
from bfgame.components.savingthrows import SavingThrows
from bfgame.components.valuable import Valuable
from bfgame.components.shield import Shield
from bfgame.components.skills import Skills
from bfgame.components.size import Size
from bfgame.components.spawninfo import SpawnInfo
from bfgame.components.specialcontainer import SpecialContainer
from bfgame.components.stats import CharacterStats
from bfgame.components.traps import Trap
from bfgame.components.wearable import Wearable
from bfgame.components.weight import Weight
from bfgame.components.vision import Vision, SimpleVision

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
    Exit.NAME,
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
