import abc


class Query(object):
    __metaclass__ = abc.ABCMeta
    """
    This object is intended to allow a type-based Query System
    for GameObjects components.
    """
    def __init__(self, querier):
        self.querier = querier
        self._result = None

    def do_query(self):
        self.querier.execute(self)
        return self.result

    @abc.abstractclassmethod
    def result(self):
        pass

    @abc.abstractclassmethod
    def name(self):
        """
        The name of the query, must be UNIQUE as it will be registered.
        """
        pass

    @abc.abstractclassmethod
    def finished(self):
        return True


class SingleQuery(Query):
    """
    This query will return as soon as it has one response.
    """
    def respond(self, value):
        self._result = value

    @property
    def finished(self):
        return bool(self.result)


class CumulativeQuery(Query):
    """
    This object will keep querying every components until the end,
    accumulating the results in a list.
    """
    def __init__(self, querier):
        super().__init__(querier)
        self._result = []

    def respond(self, value):
        self._result.append(value)

    @property
    def result(self):
        return self._result

    @property
    def finished(self):
        # This returns False so it keeps iterating until the end
        return False


class NonDefaultQuery(Query):
    """
    This query expects a value and will return the first value
    that is not equal to this default.
    """
    def __init__(self, querier, expected_result):
        super().__init__(querier)
        self.expected_result = expected_result
        self._result = None

    @property
    def result(self):
        return self.expected_result if self._result is None else self._result

    def respond(self, value):
        if value != self.expected_result:
            self._result = value

    @property
    def finished(self):
        return bool(self._result)
