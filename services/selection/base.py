class Selection(object):
    def __init__(self, executor):
        self.executor = executor
        self.resolution = None

    def resolve(self):
        """
        This is the initialization of the Selection Resolution.
        It should push its view to the director and pop itself as soon as it is resolved.
        """
        pass
