from bflib import monsters
from core.ai import behaviors
from core.ai.personalities.base import Personality
from clubsandwich.geom import Point


class Goblin(Personality):
    @classmethod
    def act(cls, host):
        # Goblins gain +1 if they see allied Warrior,
        # +2 if they see allied kings
        # A lone goblin by default will flee from anything larger than itself
        # They should roll for morale Once at first sight,
        # Adding +1 if they outnumber their opponents
        # They should roll each time a goblin is slain if there are less goblins
        # than enemies.

        # Their combat behavior is simple, Advance and Attack.
        enemies = cls.seek_enemies(host)
        if enemies:
            host_origin = Point(*host.location.get_local_coords())
            closest_enemy_point = cls.get_closest_enemy_point(host_origin, enemies)

            return behaviors.Move(host, closest_enemy_point)
            
    @classmethod
    def seek_enemies(cls, host):
        enemies = []
        for character in host.location.level.game_objects():
            if character is host:
                continue

            # TODO Factions will be taken into consideration
            # TODO Long Term State must be taken into consideration
            # TODO Anyone attacking allies are seen as enemies
            # TODO Line of Vision must be taken into consideration

            if character.monster.base_monster is monsters.Goblin:
                continue

            if not character.health.dead:
                enemies.append(character)

        return enemies

    @classmethod
    def get_closest_enemy_point(cls, origin_point, enemies):
        return origin_point.get_closest_point(
            (Point(enemy.location.get_local_coords())
             for enemy in enemies))
