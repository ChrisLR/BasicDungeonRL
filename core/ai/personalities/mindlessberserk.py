import random

from core.ai import behaviors
from core.ai.personalities.base import Personality


class MindlessBerserk(Personality):
    @classmethod
    def get_behavior(cls, host, last_behavior, short_term_state):
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
        ]
        if living_enemies:
            return host.location.point.get_closest_point(living_enemies)

    @classmethod
    def walk_somewhere_or_continue(cls, host, last_behavior):
        if last_behavior and not last_behavior.finished:
            return last_behavior

        level = host.location.level
        target_coordinate = (
            random.randint(1, level.max_x),
            random.randint(1, level.max_y)
        )

        return behaviors.Move(host, target_coordinate)
