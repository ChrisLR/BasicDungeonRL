class TargetType(object):
    name = ""


class Touch(TargetType):
    name = "Touch"


class AreaOfEffect(TargetType):
    name = "Area Of Effect"

    def __init__(self, shape, radius):
        self.shape = shape
        self.radius = radius
