from core.actions.base import Action
from core.attacks.functions import auto_attack


class Bump(Action):
    @classmethod
    def execute(cls, character, target):
        if character.combat and target.combat:
            # TODO Then if it is an ally
            # TODO Then we start an attack.
            auto_attack(character, target)

        return False
