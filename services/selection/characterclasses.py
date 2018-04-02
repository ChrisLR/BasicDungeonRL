from bflib.characters.classes import listing
from services.selection.base import Selection


class CharacterClasses(Selection):
    def resolve(self):
        self.resolution = list(listing)
