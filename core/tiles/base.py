from core.gameobject import GameObject


class Tile(GameObject):
    name = ""
    blocking = True
    opaque = True
    display = None

    def __init__(self):
        super().__init__(blocking=self.blocking, name=self.name)
        self.content = []

    def add_content(self, game_object):
        self.content.append(game_object)

    def remove_content(self, game_object):
        self.content.remove(game_object)
