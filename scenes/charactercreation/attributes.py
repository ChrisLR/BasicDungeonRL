from bearlibterminal import terminal
from clubsandwich.ui import (
    UIScene,
    SingleLineTextInputView,
    LabelView,
    ButtonView,
    LayoutOptions,
    WindowView,
)

from bflib.characters.abilityscores import AbilityScoreSet
from scenes.charactercreation.races import RaceSelectionScene
from ui.views.validatedintstepperview import ValidatedIntStepperView


class AttributeSelectionScene(UIScene):
    def __init__(self, game_context):
        self.covers_screen = True
        self.game_context = game_context
        stat_initial = 7
        stat_minimum = 3
        stat_maximum = 18

        views = [
            WindowView(title='Ability Score Selection', subviews=[
                LabelView("Name:", layout_options=LayoutOptions(**get_left_layout(2))),
                SingleLineTextInputView(
                    callback=self.set_name,
                    layout_options=LayoutOptions(**get_right_layout(3, width=0.2, right=0.4))
                ),
                LabelView("Strength:", layout_options=LayoutOptions(**get_left_layout(6))),
                ValidatedIntStepperView(
                    validation_callback=self.validate_points,
                    value=stat_initial, callback=lambda value: self.set_stat("Strength", value),
                    min_value=stat_minimum, max_value=stat_maximum,
                    layout_options=LayoutOptions(**get_right_layout(7, width=5)),
                ),
                LabelView("Dexterity:", layout_options=LayoutOptions(**get_left_layout(7))),
                ValidatedIntStepperView(
                    validation_callback=self.validate_points,
                    value=stat_initial, callback=lambda value: self.set_stat("Dexterity", value),
                    min_value=stat_minimum, max_value=stat_maximum,
                    layout_options=LayoutOptions(**get_right_layout(8, width=5)),
                ),
                LabelView("Constitution:", layout_options=LayoutOptions(**get_left_layout(8))),
                ValidatedIntStepperView(
                    validation_callback=self.validate_points,
                    value=stat_initial, callback=lambda value: self.set_stat("Constitution", value),
                    min_value=stat_minimum, max_value=stat_maximum,
                    layout_options=LayoutOptions(**get_right_layout(9, width=5)),
                ),
                LabelView("Intelligence:", layout_options=LayoutOptions(**get_left_layout(9))),
                ValidatedIntStepperView(
                    validation_callback=self.validate_points,
                    value=stat_initial, callback=lambda value: self.set_stat("Intelligence", value),
                    min_value=stat_minimum, max_value=stat_maximum,
                    layout_options=LayoutOptions(**get_right_layout(10, width=5)),
                ),
                LabelView("Charisma:", layout_options=LayoutOptions(**get_left_layout(10))),
                ValidatedIntStepperView(
                    validation_callback=self.validate_points,
                    value=stat_initial, callback=lambda value: self.set_stat("Charisma", value),
                    min_value=stat_minimum, max_value=stat_maximum,
                    layout_options=LayoutOptions(**get_right_layout(11, width=5)),
                ),
                LabelView("Wisdom:", layout_options=LayoutOptions(**get_left_layout(11))),
                ValidatedIntStepperView(
                    validation_callback=self.validate_points,
                    value=stat_initial, callback=lambda value: self.set_stat("Wisdom", value),
                    min_value=stat_minimum, max_value=stat_maximum,
                    layout_options=LayoutOptions(**get_right_layout(12, width=5))
                ),
                ButtonView('Finish', self.finish,
                           layout_options=LayoutOptions(**get_left_layout(13, left=0.45)))
            ])
        ]
        super().__init__(views)

        self.name = ""
        self.stats = {
            "strength": stat_initial,
            "dexterity": stat_initial,
            "constitution": stat_initial,
            "intelligence": stat_initial,
            "charisma": stat_initial,
            "wisdom": stat_initial
        }
        self.points_left = 18
        self.choices = {}

    def set_name(self, value):
        self.name = value

    def set_stat(self, name, value):
        self.stats[name.lower()] = value

    def validate_points(self, old_value, new_value):
        if new_value > old_value:
            point_cost = 1
            if self.points_left >= point_cost:
                self.points_left -= point_cost
                return True
        if new_value < old_value:
            point_cost = 1
            self.points_left += point_cost
            return True

        return False

    def finish(self):
        if self.points_left <= 0:
            self.director.replace_scene(RaceSelectionScene(self.game_context, AbilityScoreSet(**self.stats)))

    def terminal_read(self, val):
        super().terminal_read(val)
        if val == terminal.TK_UP:
            self.view.find_prev_responder()
        elif val == terminal.TK_DOWN:
            self.view.find_next_responder()


def get_left_layout(top, **kwargs):
    layout_options = dict(width=0.1, left=0.3, top=top, height=0.1, bottom=None, right=None)
    if kwargs:
        layout_options.update(kwargs)

    return layout_options


def get_right_layout(top, **kwargs):
    layout_options = dict(width=0.1, left=None, top=top, height=0.1, bottom=None, right=0.5)
    if kwargs:
        layout_options.update(kwargs)

    return layout_options

