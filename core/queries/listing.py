query_listing = []
query_names = set()
query_mapping = {}


def register_query(item):
    query_listing.append(item)
    query_names.add(item.name)
    query_mapping[item.name] = item

    return item


def get_by_name(name):
    return query_mapping.get(name)
