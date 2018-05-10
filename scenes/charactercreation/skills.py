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
from bflib.skills.listing import skill_listing


class SkillsSelectionScene(UIScene):
    def __init__(self, game):
        self.covers_screen = True
        self.game = game
        self.skills = {}
        self.points_left = 3
        labels = [
            (LabelView("%s:" % skill.name, layout_options=LayoutOptions(**get_left_layout(i*2))),
             for i, skill in enumerate(sorted(list(skill_listing), key=lambda skill: skill.name)))
        ]
        int_steppers = [
            (
             ValidatedIntStepperView(
                validation_callback=self.validate_points,
                value=0,
                callback=lambda value: self.set_skill(skill, value),
                layout_options=LayoutOptions(**get_right_layout(i*2, width=5)),
            )
            for i, skill in enumerate(sorted(list(skill_listing), key=lambda skill: skill.name)))
        ]
        sub_views = []
        sub_views.extend(zip(labels, int_steppers))
        sub_views.append(
            ButtonView(
                'Finish', self.finish,
                layout_options=LayoutOptions(**get_left_layout(13, left=0.45))
            ))
        views = [WindowView(title='Skill Selection', subviews=[sub_views])]
        super().__init__(views)

        self.name = ""

    def set_name(self, value):
        self.name = value

    def set_skill(self, skill, value):
        player_skills = self.game.player.skills
        point_cost = player_skills.get_increase_cost(skill)
        if self.points_left >= point_cost:
            self.skills[skill] = value
            self.points_left -= point_cost

    def validate_points(self, old_value, new_value):
        if self.points_left > 0:
            return True
        return False

    def finish(self):
        if self.points_left <= 0:
            player_skills = self.game.player.skills
            for skill, value in self.skills.items():
                player_skills.set_skill(skill, value)

            # TODO Gotta Chain this
            # self.director.replace_scene(
            #     RaceSelectionScene(
            #         game=self.game,
            #         ability_score_set=AbilityScoreSet(**self.stats),
            #         name=self.name
            #     )
            # )

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
