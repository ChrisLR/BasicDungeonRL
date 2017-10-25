from core.components import Component


class LiquidContainer(Component):
    NAME = "liquidcontainer"
    __slots__ = ["container_type", "liquid_held", "volume_limit"]

    def __init__(self, container_type, volume_limit):
        super().__init__()
        self.container_type = container_type
        self.liquid_held = []
        self.volume_limit = volume_limit

    def copy(self):
        return LiquidContainer(
            self.container_type,
            self.volume_limit,
        )
