from bflib.characters.specialabilities.base import SpecialAbility


class FeebleConstitution(SpecialAbility):
    def __init__(self, value):
        self.value = value
