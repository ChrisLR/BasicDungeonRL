import abc
import random

from core.threatlevels import ThreatLevel


class Body(object):
    @abc.abstractmethod
    def name(self):
        pass

    @abc.abstractmethod
    def base_height(self):
        pass

    @abc.abstractmethod
    def base_weight(self):
        pass

    @abc.abstractmethod
    def template_outer_material(self):
        pass

    @abc.abstractmethod
    def template_inner_material(self):
        pass

    @abc.abstractmethod
    def template_structural_material(self):
        pass

    @abc.abstractmethod
    def template_blood(self):
        pass

    def __init__(self, body_parts):
        super().__init__()
        self.outer_material = self.template_outer_material()
        self.inner_material = self.template_inner_material()
        self.structural_material = self.template_structural_material()
        self.blood = self.template_blood()
        self.body_parts = body_parts
        self.bound_abilities = {}
        self.bound_attacks = {}

    @staticmethod
    def _random_roll_body_part(body_parts):
        tries = 0
        max_tries = 3
        while tries < max_tries:
            tries += 1
            for body_part in body_parts:
                if random.randrange(0, 100) <= body_part.relative_size:
                    return body_part

        return random.choice(body_parts)

    def get_random_body_part_for_threat_level(self, threat_level):
        size_sorted_body_parts = [body_part for body_part in self.body_parts
                                  if body_part.threat_level == threat_level]
        if not size_sorted_body_parts:
            if threat_level < ThreatLevel.Fatal:
                return self.get_random_body_part_for_threat_level(
                    ThreatLevel[threat_level.value + 1])
            else:
                return self.get_random_body_part_by_relative_size()

        return self._random_roll_body_part(size_sorted_body_parts)

    def get_random_body_part_by_relative_size(self):
        size_sorted_body_parts = sorted(
            self.body_parts,
            key=lambda body_part: body_part.relative_size, reverse=True)

        return self._random_roll_body_part(size_sorted_body_parts)

    def bind_ability(self, ability, body_parts):
        self.bound_abilities[ability] = body_parts

    def bind_attack(self, attack, body_parts):
        self.bound_attacks[attack] = body_parts

    def check_attack(self, attack):
        # TODO Ideally this would also check for damaged limbs, out of scope for now.
        bound_body_parts = self.bound_attacks.get(attack)
        if bound_body_parts is not None:
            if all((bp for bp in bound_body_parts if bp in self.body_parts)):
                return True
        return False

    def check_ability(self, ability):
        # TODO Ideally this would also check for damaged limbs, out of scope for now.
        bound_body_parts = self.bound_abilities.get(ability)
        if bound_body_parts is not None:
            if all((bp for bp in bound_body_parts if bp in self.body_parts)):
                return True
        return False

    def get_attacks(self):
        return self.bound_attacks.keys()

    def get_body_parts(self):
        return self.body_parts

    def get_body_parts_with_slots(self, keyword):
        return [body_part for body_part in self.body_parts if body_part.has_item_slot(keyword)]

    def get_graspable_body_parts(self):
        return [body_part for body_part in self.body_parts if body_part.can_grasp]
