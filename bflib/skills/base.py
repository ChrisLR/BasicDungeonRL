class Skill(object):
    name = ""
    related_stat = None
    natural = False
    character_class = None

    __slots__ = ["value"]

    def __init__(self, value=0):
        self.value = value
