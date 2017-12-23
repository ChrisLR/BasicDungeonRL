from functools import partial

from clubsandwich.ui import (
    ButtonView,
    UIScene,
    LayoutOptions,
    WindowView,
)

from bflib.characters import classes
from core.displaypriority import DisplayPriority
from core.factories.character import CharacterFactory
from core.util.colors import Colors
from scenes.game.scene import GameScene
from ui.views import SelectableButtonView, KeyAssignedListView


class ClassSelectionScene(UIScene):
    _inactive_fg = '#ffffff'
    _active_fg = "#efff14"
    _disabled_fg = '#424242'

    def __init__(self, game_context, ability_score_set, name, race):
        self.covers_screen = True
        self.game_context = game_context
        self.ability_score_set = ability_score_set
        self.name = name
        self.race = race

        self.sorted_classes = sorted(classes.listing, key=lambda c_class: c_class.name)
        self.enabled_classes, self.disabled_classes = self.filter_class_choices()

        self.buttons = {
            character_class:
                SelectableButtonView(
                    character_class.name, partial(self.set_character_class, character_class),
                    color_fg=self._inactive_fg if character_class in self.enabled_classes else self._disabled_fg
                )
            for character_class in self.sorted_classes
        }
        self.class_choices = []

        views = [
            WindowView(title='Class Selection', subviews=[
                KeyAssignedListView(self.buttons.values()),
                ButtonView('Finish', self.finish,
                           layout_options=LayoutOptions(**get_left_layout(13, left=0.45)))
            ])
        ]
        super().__init__(views)

    def filter_class_choices(self):
        enabled_classes = []
        disabled_classes = []
        for character_class in self.sorted_classes:
            disabled = False
            if self.race.restriction_set.classes and not self.race.restriction_set.classes.evaluate(character_class):
                disabled = True
            if character_class.restriction_set.ability_score and not character_class.restriction_set.ability_score.evaluate(self.ability_score_set):
                disabled = True

            if disabled:
                disabled_classes.append(character_class)
            else:
                enabled_classes.append(character_class)

        return enabled_classes, disabled_classes

    def deselect_class(self, character_class):
        self.class_choices.remove(character_class)
        button = self.buttons[character_class]
        button.deselect()

    def select_class(self, character_class):
        self.class_choices.append(character_class)
        button = self.buttons[character_class]
        button.select()

    def set_character_class(self, value):
        if value not in self.disabled_classes:
            if value in self.class_choices:
                self.deselect_class(value)
            else:
                if self.race.restriction_set.classes.access_combined:
                    if len(self.class_choices) < 2:
                        self.select_class(value)
                else:
                    if self.class_choices:
                        self.deselect_class(self.class_choices[0])
                    self.select_class(value)

    def finish(self):
        if not self.class_choices:
            return

        player = CharacterFactory.create_new(
            ability_score_set=self.ability_score_set,
            base_classes=self.class_choices,
            base_race=self.race,
            name=self.name,
            symbol="@",
            fg_color=Colors.WHITE,
            bg_color=Colors.BLACK,
            display_priority=DisplayPriority.Player
        )

        self.game_context.player = player
        self.director.replace_scene(GameScene(self.game_context))


def get_left_layout(top, **kwargs):
    layout_options = dict(width=0.1, left=0.3, top=top, height=0.1, bottom=None, right=None)
    if kwargs:
        layout_options.update(kwargs)

    return layout_options
