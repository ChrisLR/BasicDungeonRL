from clubsandwich.ui import LayoutOptions
from clubsandwich.ui import UIScene, WindowView

from core import actionmapping
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
        self.hud_view = HudView(game_context, layout_options=hud_view_layout_options)
        super().__init__(WindowView("", subviews=[self.hud_view, self.game_view, self.console]))

    def terminal_read(self, val):
        action = actionmapping.lowercase_mapping.get(val, None)
        if action:
            if action.target_selection_type:
                def execute(targets):
                    if action.can_execute(self.game_context.player, targets):
                        action.execute(self.game_context.player, targets)
                        self.update_turn()

                selection_screen = action.target_selection_type.select(
                    self.game_context.player, action.target_type, execute)
                self.director.push_scene(selection_screen)
                return

            else:
                if action.can_execute(self.game_context.player):
                    action.execute(self.game_context.player)

        self.update_turn()

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
