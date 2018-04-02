from core.components.base import Component


class Effects(Component):
    NAME = "effects"
    __slots__ = ["active_effects", "finished_effects"]

    def __init__(self):
        super().__init__()
        self.active_effects = {}
        self.finished_effects = []

    def add_effect(self, effect):
        if not self.has_effect(type(effect)):
            self.active_effects[type(effect)] = effect
            effect.on_start(self.host)

    def has_effect(self, effect_type):
        return effect_type in self.active_effects

    def remove_effect(self, effect_type):
        if self.has_effect(effect_type):
            effect_instance = self.active_effects.get(effect_type)
            effect_instance.on_finish(self.host)
            del self.active_effects[effect_type]

    def round_update(self):
        for effect in self.finished_effects:
            self.remove_effect(type(effect))

        for effect in self.active_effects.values():
            effect.update(self.host)

        self.finished_effects = [effect for effect in self.active_effects if effect.finished]

    def copy(self):
        return Effects()
