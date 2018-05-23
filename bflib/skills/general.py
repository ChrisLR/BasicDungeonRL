from bflib.skills.base import Skill
from bflib.characters import abilityscores
from bflib.skills import listing


@listing.register
class Appraise(Skill):
    name = "Appraise"
    related_stat = abilityscores.Intelligence
    natural = True


@listing.register
class Diplomacy(Skill):
    name = "Diplomacy"
    related_stat = abilityscores.Charisma
    natural = True


@listing.register
class HandleAnimal(Skill):
    name = "Handle Animal"
    related_stat = abilityscores.Charisma
    natural = True


@listing.register
class Jump(Skill):
    name = "Jump"
    related_stat = abilityscores.Strength
    natural = True


@listing.register
class Ride(Skill):
    name = "Ride"
    related_stat = abilityscores.Dexterity
    natural = True


@listing.register
class SenseMotive(Skill):
    name = "Sense Motive"
    related_stat = abilityscores.Wisdom
    natural = True


@listing.register
class Spot(Skill):
    name = "Spot"
    related_stat = abilityscores.Wisdom
    natural = True


@listing.register
class Survival(Skill):
    name = "Survival"
    related_stat = abilityscores.Wisdom
    natural = True


@listing.register
class Swim(Skill):
    name = "Swim"
    related_stat = abilityscores.Strength
    natural = False
