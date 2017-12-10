from core.ai.personalities.base import Personality


class Goblin(Personality):
    def act(self, host):
        # Goblins gain +1 if they see allied Warrior,
        # +2 if they see allied kings
        # A lone goblin by default will flee from anything larger than itself
        # They should roll for morale Once at first sight,
        # Adding +1 if they outnumber their opponents
        # They should roll each time a goblin is slain if there are less goblins
        # than enemies.

        # Their combat behavior is simple, Advance and Attack.
        pass
