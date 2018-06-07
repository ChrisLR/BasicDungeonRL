"""
A team consist of a band of characters that may or may not share factions.
As long as there are no hostilities within the team.
Any member's individual action affects the entire team's reputation.
"""


class Team(object):
    def __init__(self):
        self.members = set()
        self.enemy_objects = set()

    def make_member(self, game_object):
        if game_object in self.enemy_objects:
            self.enemy_objects.remove(game_object)
        self.members.add(game_object)

    def make_enemy(self, game_object):
        if game_object in self.members:
            self.members.remove(game_object)
        self.enemy_objects.add(game_object)

    def is_allied(self, game_object):
        if game_object in self.members:
            return True

    def is_enemy(self, game_object):
        if game_object in self.members:
            return False

        alliance = game_object.alliance
        if not alliance:
            return False

        member_alliances = {game_object.alliance for game_object in self.members}
        if any(faction for faction in alliance.factions
               if any(alliance for alliance in member_alliances
                      if alliance.is_enemy(faction))):
            return True

        return False
