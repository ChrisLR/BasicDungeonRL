from functools import partial

from clubsandwich.ui import (
    UIScene,
    ButtonView,
    LayoutOptions,
    WindowView,
)

from bflib.characters import races
from scenes.charactercreation.classes import ClassSelectionScene
from ui.views import KeyAssignedListView, SelectableButtonView


class RaceSelectionScene(UIScene):
    _inactive_fg = '#ffffff'
    _active_fg = "#efff14"
    _disabled_fg = '#424242'

    def __init__(self, game_context, ability_score_set, name):
        self.covers_screen = True
        self.game_context = game_context
        self.ability_score_set = ability_score_set
        self.name = name

        self.sorted_races = sorted(races.listing, key=lambda race: race.name)
        self.enabled_races, self.disabled_races = self.filter_race_choices()

        self.buttons = {
            race:
                SelectableButtonView(
                    race.name, partial(self.set_race, race),
                    color_fg=self._inactive_fg if race in self.enabled_races else self._disabled_fg
                )
            for race in self.sorted_races
        }
        self.race_choice = None

        views = [
            WindowView(title='Race Selection', subviews=[
                KeyAssignedListView(self.buttons.values()),
                ButtonView('Finish', self.finish,
                           layout_options=LayoutOptions(**get_left_layout(13, left=0.45)))
            ])
        ]
        super().__init__(views)

    def filter_race_choices(self):
        enabled_races = []
        disabled_races = []
        for race in self.sorted_races:
            if race.restriction_set.ability_score \
                    and not race.restriction_set.ability_score.evaluate(self.ability_score_set):
                disabled_races.append(race)
            else:
                enabled_races.append(race)

        return enabled_races, disabled_races

    def deselect_race(self, race):
        self.race_choice = None
        button = self.buttons[race]
        button.deselect()

    def select_race(self, race):
        self.race_choice = race
        button = self.buttons[race]
        button.select()

    def set_race(self, value):
        if value not in self.disabled_races:
            if self.race_choice:
                self.deselect_race(self.race_choice)
            self.select_race(value)

    def finish(self):
        if not self.race_choice:
            return

        self.director.replace_scene(
            ClassSelectionScene(
                game_context=self.game_context,
                ability_score_set=self.ability_score_set,
                name=self.name,
                race=self.race_choice
            )
        )


def get_left_layout(top, **kwargs):
    layout_options = dict(width=0.1, left=0.3, top=top, height=0.1, bottom=None, right=None)
    if kwargs:
        layout_options.update(kwargs)

    return layout_options
