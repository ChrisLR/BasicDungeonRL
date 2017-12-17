from bflib import monsters
from core.ai import behaviors
from core.ai.personalities.base import Personality
from clubsandwich.geom import Point
import random


class Goblin(Personality):
    @classmethod
    def get_behavior(cls, host, last_behavior):
        # Goblins gain +1 if they see allied Warrior,
        # +2 if they see allied kings
        # A lone goblin by default will flee from anything larger than itself
        # They should roll for morale Once at first sight,
        # Adding +1 if they outnumber their opponents
        # They should roll each time a goblin is slain if there are less goblins
        # than enemies.

        # Their combat behavior is simple, Advance and Attack.
        immediate_enemies = cls.seek_immediate_threat(host)
        if immediate_enemies:
            return cls.engage_immediate_enemies(host, immediate_enemies, last_behavior)

        return cls.walk_somewhere_or_continue(host, last_behavior)

    @classmethod
    def seek_immediate_threat(cls, host):
        enemies = []
        for character in host.location.level.game_objects:
            if character is host:
                continue

            # TODO Factions will be taken into consideration
            # TODO Long Term State must be taken into consideration
            # TODO Anyone attacking allies are seen as enemies
            # TODO Line of Vision must be taken into consideration

            if character.monster.base_monster is monsters.Goblin:
                continue

            if character.health.dead:
                continue

            if host.location.point.manhattan_distance_to(character.location.point) < 10:
                enemies.append(character)

        return enemies

    @classmethod
    def engage_immediate_enemies(cls, host, enemies, last_behavior):
        target_point = cls.get_closest_enemy_point(host, enemies)
        target_coordinate = (target_point.x, target_point.y)
        if isinstance(last_behavior, behaviors.Move):
            last_behavior.adjust_target_coordinates(target_coordinate)
            return last_behavior
        return behaviors.Move(host, target_coordinate, True)

    @classmethod
    def get_closest_enemy_point(cls, host, enemies):
        return host.location.point.get_closest_point(
            [enemy.location.point for enemy in enemies])

    @classmethod
    def walk_somewhere_or_continue(cls, host, last_behavior):
        if last_behavior:
            return last_behavior

        level = host.location.level
        target_coordinate = random.randint(1, level.max_x), random.randint(1, level.max_y)

        return behaviors.Move(host, target_coordinate, False)
