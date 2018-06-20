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
        self.game = None

    def on_register(self, host):
        super().on_register(host)
        self.game = host.game

    def get_draw_info(self):
        bg_color = terminal.color_from_argb(255, *self.background_color)
        if self.game:
            player = self.game.player
            if not player is self.host:
                player_alliance = player.alliance
                if player_alliance and player_alliance.is_allied(self.host):
                    bg_color = terminal.color_from_argb(255, 0, 0, 125)
        color = terminal.color_from_argb(255, *self.foreground_color)

        return "[color={}][bkcolor={}]{}".format(color, bg_color, self.ascii_character)

    def copy(self):
        new_instance = Display(self.foreground_color, self.background_color, self.ascii_character)
        return new_instance
