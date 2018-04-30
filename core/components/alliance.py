from core.components.base import Component


class Alliance(Component):
    NAME = 'alliance'
    __slots__ = ["effects"]

    def __init__(self, personal_hostiles=None, factions=None, team=None):
        super().__init__()
        self.personal_hostiles = personal_hostiles or set()
        self.factions = factions or set()
        self.team = team

    def is_allied(self, game_object):
        # TODO Object must not be in personal hostiles, must share at least one faction but not be in any enemy faction
        # or be in the same team.
        pass

    def is_neutral(self, game_object):
        # TODO Object must not be in personal hostiles nor enemy of any factions
        pass

    def is_enemy(self, game_object):
        # TODO Object is known hostile by personal, faction or team.
        pass

    def copy(self):
        return Alliance(self.personal_hostiles, self.factions, self.team)
