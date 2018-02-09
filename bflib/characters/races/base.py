import abc
from datetime import timedelta

from bflib import languages, restrictions, units
from bflib.characters import specialabilities, savingthrows
from bflib.keywords.items import WearLocation, WieldLocation


class Race(object):
    __metaclass__ = abc.ABCMeta

    name = ""
    average_height = units.Feet(0)
    average_weight = units.Pound(0)
    average_lifespan = timedelta(0)

    restriction_set = restrictions.RestrictionSet()
    racial_class = None
    racial_language = languages.Common
    size = None
    special_ability_set = specialabilities.SpecialAbilitySet()
    saving_throw_set = savingthrows.SavingThrowSet()

    wear_locations = (
        WearLocation.Head,
        WearLocation.Face,
        WearLocation.Neck,
        WearLocation.Torso,
        WearLocation.Arms,
        WearLocation.Arms,
        WearLocation.Hands,
        WearLocation.Hands,
        WearLocation.Rings,
        WearLocation.Rings,
        WearLocation.Legs,
        WearLocation.Legs,
        WearLocation.Feet,
        WearLocation.Feet,
        WearLocation.Bandolier,
        WearLocation.Back,
        WearLocation.Belt,
        WearLocation.Waist,
    )

    wield_locations = (
        WieldLocation.LeftHand,
        WieldLocation.RightHand,
    )
