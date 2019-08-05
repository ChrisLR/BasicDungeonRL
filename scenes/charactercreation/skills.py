from functools import partial

from bearlibterminal import terminal
from clubsandwich.ui import (
    LabelView,
    ButtonView,
    LayoutOptions,
    WindowView,
)

from bflib.skills.listing import skill_listing
from core.ui import CoreUIScene
from core.ui.views import ValidatedIntStepperView


class SkillsSelection(CoreUIScene):
    def __init__(self, game):
        self.covers_screen = True
        self.game = game
        self.skills = {}
        self.points_left = 3
        self.player = self.game.player
        self.player_skills = self.player.skills
        self.game.player = self.player
        self.manager = None

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
                callback=partial(self.set_skill, skill=skill),
                layout_options=LayoutOptions(**get_right_layout(i+1, width=5))))

        sub_views.append(
            ButtonView(
                'Finish', self.finish,
                layout_options=LayoutOptions(**get_left_layout(0.9, left=0.45))
            ))
        views = [WindowView(title='Skill Selection', subviews=sub_views)]
        super().__init__(views)

    def set_skill(self, value, skill):
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
            self.manager.next()

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
