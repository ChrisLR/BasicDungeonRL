from clubsandwich.ui import LayoutOptions
from clubsandwich.ui import UIScene, WindowView

from core import actionmapping
from core.actions.stack import ActionStack
from scenes.game.views.game import GameView
from scenes.game.views.hud import HudView
from services.echo.service import echo_service
from ui.views import ScrollingTextView


class GameScene(UIScene):
    def __init__(self, game_context):
        console_layout_options = LayoutOptions(top=None, height=12, bottom=0, left=1, right=None, width=0.98)
        game_view_layout_options = LayoutOptions(top=10, height=30, bottom=None, left=0, right=None, width=1)
        hud_view_layout_options = LayoutOptions(top=0, height=10, bottom=None, left=0, right=None, width=1)
        self.console = ScrollingTextView(12, 110, layout_options=console_layout_options)
        echo_service.console = self.console
        game_context.game.new_game()
        self.game_view = GameView(game_context, layout_options=game_view_layout_options)
        self.game_context = game_context
        game_context.action_stack = ActionStack(game_context.player, self.update_turn)
        self.hud_view = HudView(game_context, layout_options=hud_view_layout_options)
        super().__init__(WindowView("", subviews=[self.hud_view, self.game_view, self.console]))

    def terminal_update(self, is_active=False):
        super().terminal_update(is_active)
        if is_active:
            self.game_context.action_stack.update()

    def terminal_read(self, val):
        action = actionmapping.lowercase_mapping.get(val, None)
        if action:
            self.game_context.action_stack.add_action_to_stack(action)

    def update_turn(self):
        time_update_result = self.game_context.game_time.pass_turns()
        current_level = self.game_context.player.location.level
        game_objects = current_level.game_objects
        game_objects.append(self.game_context.player)
        for i in range(len(game_objects) - 1, -1, -1):
            game_object = game_objects[i]
            game_object.round_update()

            if time_update_result.minute_updated:
                game_object.minute_update()

            if time_update_result.hours_updated:
                game_object.hours_update()

            if time_update_result.days_updated:
                game_object.days_update()
