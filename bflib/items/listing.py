item_listing = set()
item_types = set()
__items_by_type = {}


def register_item(item):
    __items_by_type.clear()
    item_listing.add(item)

    return item


def register_type(item_type):
    __items_by_type.clear()
    item_types.add(item_type)

    return item_type


def get_items_by_type(type_filter=None):
    __rebuild_cached_items_by_type()
    if type_filter:
        return __items_by_type[type_filter]
    return __items_by_type


def __rebuild_cached_items_by_type():
    if __items_by_type:
        return

    for item_type in item_types:
        __items_by_type[item_type] = set()
        for item in item_listing:
            if issubclass(item, item_type):
                __items_by_type[item_type].add(item)
