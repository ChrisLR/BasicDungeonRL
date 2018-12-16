from bfgame.components.base import Component
from core.queries import listing


class Query(Component):
    NAME = "query"
    __slots__ = ["mapping"]

    def __init__(self):
        super().__init__()
        self.mapping = {}
        self.initialize_query_types()

    def initialize_query_types(self):
        for query in listing.query_listing:
            self.mapping[query] = {}

    def register_responder(self, query_type, responder, func):
        self.mapping[query_type][responder] = func

    def unregister_responder(self, query_type, responder):
        del self.mapping[query_type][responder]

    def execute(self, query):
        query_type = type(query)
        responders = self.mapping.get(query_type)
        for _, func in responders.items():
            func(query)
            if query.finished:
                return query.result
        return query.result

    def __getattr__(self, item):
        query_type = listing.get_by_name(item)
        if query_type is None:
            raise AttributeError("No queries by the name {}".format(item))

        return query_type(self).do_query

    def copy(self):
        return Query()
