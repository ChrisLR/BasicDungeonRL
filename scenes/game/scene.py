import time

from bearlibterminal import terminal
from clubsandwich.ui import LayoutOptions
from clubsandwich.ui import UIScene, WindowView

from core.actions.basestack import ActionStack
from scenes.game.views.game import GameView
from scenes.game.views.hud import HudView
from ui.views import ScrollingTextView


class GameScene(UIScene):
    def __init__(self, game):
        console_layout_options = LayoutOptions(top=None, height=12, bottom=0, left=1, right=None, width=0.99)
        game_view_layout_options = LayoutOptions(top=10, height=30, bottom=None, left=0, right=None, width=0.99)
        hud_view_layout_options = LayoutOptions(top=0, height=0.2, bottom=None, left=0, right=None, width=0.99)
        self.console = ScrollingTextView(12, 110, layout_options=console_layout_options)
        self.game_view = GameView(game, layout_options=game_view_layout_options)
        self.game = game
        game.action_stack = ActionStack(game, game.player, self.update_turn)
        self.hud_view = HudView(game, layout_options=hud_view_layout_options)
        super().__init__(WindowView("", subviews=[self.hud_view, self.game_view, self.console]))
        self.game.player.vision.update_field_of_vision()
        self.game.game_scene = self

    def terminal_update(self, is_active=False):
        super().terminal_update(is_active)
        if is_active:
            self.game.action_stack.update()

        player_health = self.game.player.health
        if player_health and not player_health.conscious:
            time.sleep(1)
            self.update_turn()

        messages = self.game.echo.messages
        if messages:
            for message in messages:
                self.console.add_lines(message)
            messages.clear()

    def terminal_read(self, val):
        self.game.director = self.director
        player = self.game.player
        player_health = player.health
        if val == terminal.TK_F1:
            self.game.loop.quit()

        if player_health.dead or not player_health.conscious:
            return
        
        if terminal.state(terminal.TK_SHIFT):
            action = self.game.action_mapping.get_uppercase(val)
        else:
            action = self.game.action_mapping.get_lowercase(val)

        if action:
            self.game.action_stack.add_action_to_stack(action)

    def update_turn(self):
        time_update_result = self.game.game_time.pass_turns()
        current_level = self.game.player.location.level
        game_objects = list(current_level.game_objects)
        for game_object in game_objects:
            game_object.round_update()

            if time_update_result.minute_updated:
                game_object.minute_update()

            if time_update_result.hours_updated:
                game_object.hours_update()

            if time_update_result.days_updated:
                game_object.days_update()

        self.game.player.vision.update_field_of_vision()
