class ShortTermState(object):
    """
    This object will represent the short term state of an AI.
    Examples
    - A temporary Alliance
    - Alertness Level.
    - Emotions such as Anger, happiness.
    """

    def __init__(self):
        self.allies = set()
        self.enemies = set()
        self.neutrals = set()
        self.known_objects = set()

    def add_ally(self, game_object):
        self.allies.add(game_object)
        self.known_objects.add(game_object)

    def add_enemy(self, game_object):
        self.enemies.add(game_object)
        self.known_objects.add(game_object)

    def add_neutral(self, game_object):
        self.neutrals.add(game_object)
        self.known_objects.add(game_object)
