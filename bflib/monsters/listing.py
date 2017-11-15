monster_listing = set()
monster_types = set()
__monsters_by_type = {}


def register_monster(monster):
    __monsters_by_type.clear()
    monster_listing.add(monster)

    return monster


def register_type(monster_type):
    __monsters_by_type.clear()
    monster_types.add(monster_type)

    return monster_type


def get_monsters_by_type(type_filter=None):
    __rebuild_cached_items_by_type()
    if type_filter:
        return __monsters_by_type[type_filter]
    return __monsters_by_type


def __rebuild_cached_items_by_type():
    if __monsters_by_type:
        return

    for monster_type in monster_types:
        __monsters_by_type[monster_type] = set()
        for item in monster_listing:
            if issubclass(item, monster_type):
                __monsters_by_type[monster_type].add(item)
