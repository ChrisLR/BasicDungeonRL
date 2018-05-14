from bearlibterminal import terminal
from clubsandwich.ui import (
    UIScene,
    LabelView,
    ButtonView,
    LayoutOptions,
    WindowView,
)

from bflib.skills.listing import skill_listing
from core import components
from core.displaypriority import DisplayPriority
from core.util.colors import Colors
from ui.views.validatedintstepperview import ValidatedIntStepperView
from functools import partial


class SkillsSelectionScene(UIScene):
    def __init__(self, game, ability_score_set, class_choices, race, name):
        self.covers_screen = True
        self.game = game
        self.skills = {}
        self.points_left = 3
        self.ability_score_set = ability_score_set
        self.class_choices = class_choices
        self.race = race
        self.name = name
        self.player = self.game.factory.create_new_character(
            ability_score_set=self.ability_score_set,
            base_classes=self.class_choices,
            base_race=self.race,
            name=self.name,
            symbol="@",
            fg_color=Colors.WHITE,
            bg_color=Colors.BLACK,
            display_priority=DisplayPriority.Player
        )
        self.player.register_component(components.Player())
        self.player.register_component(components.Skills())
        self.player_skills = self.player.skills
        self.game.player = self.player

        sorted_skills = sorted(list(skill_listing), key=lambda skill: skill.name)
        sub_views = []
        for i, skill in enumerate(sorted_skills):
            partial_validation = partial(self.validate_points, skill=skill)
            sub_views.append(
                LabelView("%s:" % skill.name,
                          layout_options=LayoutOptions(**get_left_layout(i))))
            sub_views.append(ValidatedIntStepperView(
                validation_callback=partial_validation,
                value=0,
                callback=lambda value: self.set_skill(skill, value),
                layout_options=LayoutOptions(**get_right_layout(i+1, width=5))))

        sub_views.append(
            ButtonView(
                'Finish', self.finish,
                layout_options=LayoutOptions(**get_left_layout(0.9, left=0.45))
            ))
        views = [WindowView(title='Skill Selection', subviews=sub_views)]
        super().__init__(views)

        self.name = ""

    def set_name(self, value):
        self.name = value

    def set_skill(self, skill, value):
        self.skills[skill] = value

    def validate_points(self, old_value, new_value, skill):
        point_cost = self.player_skills.get_increase_cost(skill)
        if new_value < 0:
            return False

        if new_value > old_value:
            if self.points_left >= point_cost:
                self.points_left -= point_cost
                return True

        if new_value < old_value:
            self.points_left += point_cost
            return True

        return False

    def finish(self):
        if self.points_left <= 0:
            for skill, value in self.skills.items():
                self.player_skills.set_skill(skill, value)
            self.game.new_game()

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
