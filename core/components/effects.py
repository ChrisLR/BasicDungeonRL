from core.components.base import Component


class Effects(Component):
    NAME = "effects"
    __slots__ = ["active_effects", "finished_effects"]

    def __init__(self):
        super().__init__()
        self.active_effects = []
        self.finished_effects = []

    def add_effect(self, effect):
        self.active_effects.append(effect)
        effect.on_start(self.host)

    def round_update(self):
        for effect in self.finished_effects:
            effect.on_finish(self.host)
            self.active_effects.remove(effect)

        for effect in self.active_effects:
            effect.update(self.host)

        self.finished_effects = [effect for effect in self.active_effects if effect.finished]

    def copy(self):
        return Effects()
