from bearlibterminal import terminal

from core.components.base import Component


class Display(Component):
    NAME = "display"
    __slots__ = ["foreground_color", "background_color", "ascii_character", "priority"]

    def __init__(self, foreground_color, background_color, ascii_character, priority=1):
        super().__init__()
        self.foreground_color = foreground_color
        self.background_color = background_color
        self.ascii_character = ascii_character
        self.priority = priority

    def get_draw_info(self):
        color = terminal.color_from_argb(255, *self.foreground_color)
        return "[color={}]{}".format(color, self.ascii_character)

    def copy(self):
        new_instance = Display(self.foreground_color, self.background_color, self.ascii_character)
        return new_instance
