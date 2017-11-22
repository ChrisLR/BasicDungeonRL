spell_listing = set()
__spells_by_class_levels = {}


def register_spell(spell):
    spell_listing.add(spell)
    for _class, _level in spell.class_level_map:
        if _class not in __spells_by_class_levels:
            __spells_by_class_levels[_class] = {}
        __spells_by_class_levels[_class][_level] = spell

    return spell


def get_spells_by_class(character_class):
    return __spells_by_class_levels.get(character_class)


def get_spells_by_class_and_levels(character_class, level):
    class_spells = get_spells_by_class(character_class)
    if class_spells is not None:
        return class_spells.get(level)

    return None

