from core.gameobject import GameObject


class Tile(GameObject):
    name = ""
    blocking = True
    opaque = True
    display = None

    def __init__(self, game):
        super().__init__(game=game, blocking=self.blocking, name=self.name)
        self.content = []

    def add_content(self, game_object):
        self.content.append(game_object)

    def remove_content(self, game_object):
        self.content.remove(game_object)
