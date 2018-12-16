from bearlibterminal import terminal
from clubsandwich.ui.ui_scene import UIScene


class CoreUIScene(UIScene):
    def terminal_read(self, val):
        # This fixes incorrectly trying to print debug info
        if val != terminal.TK_BACKSLASH:
            super().terminal_read(val)
