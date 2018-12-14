import random

from bflib import dice, monsters
from bfgame.ai import behaviors
from bfgame.ai.personalities.base import Personality


class Goblin(Personality):
    @classmethod
    def get_behavior(cls, host, last_behavior, short_term_state):
        # Goblins gain +1 if they see allied Warrior,
        # +2 if they see allied kings
        # A lone goblin by default will flee from anything larger than itself
        # They should roll for morale Once at first sight,
        # Adding +1 if they outnumber their opponents
        # They should roll each time a goblin is slain if there are less goblins
        # than enemies.

        # Their combat behavior is simple, Advance and Attack.
        cls.seek_threats(host, short_term_state)
        if short_term_state.enemies:
            target_point = cls.get_closest_enemy_point(
                host, short_term_state.enemies)
            if target_point is not None:
                distance = target_point.manhattan_distance_to(host.location.point)
                if distance < 10:
                    return cls.engage_immediate_enemies(
                        host, target_point, distance, last_behavior)

        return cls.walk_somewhere_or_continue(host, last_behavior)

    @classmethod
    def seek_threats(cls, host, short_term_state):
        unknown_objects = host.location.level.game_objects.difference(
            short_term_state.known_objects
        )
        for unknown_object in unknown_objects:
            cls.identify_relation(host, unknown_object, short_term_state)

    @classmethod
    def identify_relation(cls, host, game_object, short_term_state):
        if host is game_object:
            short_term_state.known_objects.add(host)
            return

        # TODO Factions will be taken into consideration
        # TODO Long Term State must be taken into consideration
        # TODO Anyone attacking allies are seen as enemies
        # TODO Line of Vision must be taken into consideration

        if game_object.monster.base_monster is monsters.Goblin:
            short_term_state.add_ally(game_object)
            return

        if game_object.combat and game_object.health:
            short_term_state.add_enemy(game_object)

    @classmethod
    def engage_immediate_enemies(cls, host, target_point, distance, last_behavior):
        target_coordinate = (target_point.x, target_point.y)
        if distance <= 1:
            return behaviors.MeleeAttack(host, target_point)

        if isinstance(last_behavior, behaviors.Move):
            last_behavior.adjust_target_coordinates(target_coordinate)
            return last_behavior
        return behaviors.Move(host, target_coordinate)

    @classmethod
    def get_closest_enemy_point(cls, host, enemies):
        living_enemies = [
            enemy.location.point
            for enemy in enemies
            if enemy.health.dead is False
            and host.vision.can_see_object(enemy)
        ]
        if living_enemies:
            return host.location.point.get_closest_point(living_enemies)

    @classmethod
    def walk_somewhere_or_continue(cls, host, last_behavior):
        if last_behavior and not last_behavior.finished:
            return last_behavior

        if random.randint(0, 100) < 10:
            level = host.location.level
            target_coordinate = (
                random.randint(1, level.max_x),
                random.randint(1, level.max_y)
            )
    
            return behaviors.Move(host, target_coordinate)
        else:
            return behaviors.Wait(host, dice.D6(1))
