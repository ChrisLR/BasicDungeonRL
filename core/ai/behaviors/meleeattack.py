from core.ai.behaviors.base import Behavior
from core.attacks.functions import auto_attack


class MeleeAttack(Behavior):
    def __init__(self, host, target_coordinates):
        super().__init__(host)
        self.target_coordinates = target_coordinates
        self.finished = False

    def execute(self):
        level = self.host.location.level
        game_objects = level.get_objects_by_coordinates(self.target_coordinates)
        enemies = self.host.ai.short_term_state.enemies
        enemy = next((enemy for enemy in game_objects if enemy in enemies), None)
        if enemy and not enemy.health.dead:
            auto_attack(self.host, enemy)
        self.finished = True
