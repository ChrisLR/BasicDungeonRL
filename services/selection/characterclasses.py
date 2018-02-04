from bflib.characters.classes import listing
from services.selection.base import Selection


class CharacterClasses(Selection):
    def __init__(self, executor):
        super().__init__(executor)
        self.view = None

    def resolve(self):
        self.resolution = list(listing)
