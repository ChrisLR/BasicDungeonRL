from services.selection.base import Selection


class UsableAbilities(Selection):
    """
    This selects all abilities a character can use.
    """
    def resolve(self):
        self.resolution = list(self.game.abilities.get_abilities())
