from core.components.base import Component


class Body(Component):
    NAME = "body"
    __slots__ = ["body"]

    def __init__(self, body):
        super().__init__()
        self.body = body

    def check_ability(self, ability):
        return self.body.check_ability(ability)

    def copy(self):
        return Body(type(self.body)())
