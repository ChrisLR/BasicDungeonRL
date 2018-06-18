"""
A Faction is a group representing a wide set of characteristics.

Could be Civilized, Racial or something as precise as Goblins of the yellow pants.

Factions will keep reputation of game objects or other factions.
Civilized would oppose Undeads but they could reject any single character that has attacked them.

Factions should also have rules on what actions they consider favorable or not.

Attacking an enemy faction could Add Reputation while attacking an allied or the same faction Reduces it.
At some reputation the character is banished, more than that it can be set as hostile.

Some reputations scores
 1000 could be loved
    0 could be tolerated
-1000 could be hated
"""


class Faction(object):
    def __init__(self, reputation_rules=None, enemy_factions=None, allied_factions=None):
        self.name = ""
        self.reputation_rules = reputation_rules
        self.enemy_factions = enemy_factions or set()
        self.allied_factions = allied_factions or set()
        self.enemy_objects = set()
        self.members = set()

    def add_member(self, game_object):
        self.members.add(game_object)

    def add_enemy_object(self, game_object):
        self.enemy_objects.add(game_object)

    def is_allied(self, game_object):
        if game_object in self.enemy_objects:
            return False

        alliance = game_object.alliance
        if alliance is None:
            return False

        if self._any_factions_in(alliance.factions, self.enemy_factions):
            return False

        if self._any_factions_in(alliance.factions, self.allied_factions):
            return True

        return False

    def is_enemy(self, game_object):
        if game_object in self.enemy_objects:
            return True

        alliance = game_object.alliance
        if alliance is None:
            return False

        if self._any_factions_in(alliance.factions, self.enemy_factions):
            return True

        return False

    def _any_factions_in(self, factions, faction_set):
        if factions:
            return any(faction for faction in factions if faction in faction_set)
        return False

    def add_ally_faction(self, faction):
        self.allied_factions.add(faction)

    def add_enemy_faction(self, faction):
        self.enemy_factions.add(faction)
