from bfgame.components.base import Component


class Body(Component):
    NAME = "body"
    __slots__ = ["body"]

    def __init__(self, body):
        super().__init__()
        self.body = body

    def check_ability(self, ability):
        return self.body.check_ability(ability)

    def get_attacks(self):
        return self.body.get_attacks()

    def get_body_parts(self):
        return self.body.get_body_parts()

    def get_body_parts_with_slots(self, keyword):
        return self.body.get_body_parts_with_slots(keyword)

    def get_graspable_body_parts(self):
        return self.body.get_graspable_body_parts()

    def copy(self):
        return Body(type(self.body)())
