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
        if game_object in self.personal_hostiles:
            return False

        if self.team.is_allied(game_object):
            return True

        faction_ally = False
        for faction in self.factions:
            if faction.is_allied(game_object):
                faction_ally = True
            elif faction.is_enemy(game_object):
                return False

        return faction_ally

    def is_enemy(self, game_object):
        if game_object in self.personal_hostiles:
            return True

        if self.team.is_allied(game_object):
            return False

        for faction in self.factions:
            if faction.is_enemy(game_object):
                return True

        return False

    def copy(self):
        return Alliance(self.personal_hostiles, self.factions, self.team)
