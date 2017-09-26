from clubsandwich.ui import LayoutOptions
from clubsandwich.ui import UIScene, ScrollingTextView, WindowView
from scenes.game.views.game import GameView
from scenes.game.views.hud import HudView
from core import actionmapping


class GameScene(UIScene):
    def __init__(self, game_context):
        console_layout_options = LayoutOptions(top=None, height=12, bottom=0, left=1, right=None, width=0.98)
        game_view_layout_options = LayoutOptions(top=10, height=30, bottom=None, left=0, right=None, width=1)
        hud_view_layout_options = LayoutOptions(top=0, height=10, bottom=None, left=0, right=None, width=1)
        self.console = ScrollingTextView(12, 110, layout_options=console_layout_options)

        game_context.game.new_game()
        self.game_view = GameView(game_context, layout_options=game_view_layout_options)
        self.game_context = game_context
        self.hud_view = HudView(game_context, layout_options=hud_view_layout_options)
        super().__init__(WindowView("", subviews=[self.hud_view, self.game_view, self.console]))

    def terminal_read(self, val):
        action = actionmapping.lowercase_mapping.get(val, None)
        if action:
            action.can_execute(self.game_context.player)
            action.execute(self.game_context.player)

    def update_turn(self, player):
        pass
