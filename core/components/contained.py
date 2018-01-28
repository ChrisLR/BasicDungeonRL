from bflib import units
from core.components.base import Component


class Contained(Component):
    NAME = "contained"
    __slots__ = ["parent_container"]

    def __init__(self, parent_container):
        super().__init__()
        self.parent_container = parent_container

    def copy(self):
        return Contained(
            self.parent_container
        )
