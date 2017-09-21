from clubsandwich.ui import LayoutOptions
from clubsandwich.ui.misc_views import LabelView, ButtonView
from clubsandwich.ui.ui_scene import UIScene

from scenes.charactercreation.attributes import AttributeSelectionScene


class MainMenuScene(UIScene):
    ID = "MainMenu"

    def __init__(self, game_context):
        self.covers_screen = True
        views = [
            LabelView(
                text="Placeholder Text for BasicDungeon",
                layout_options=LayoutOptions(top=0.4, height=0.1, left=None, bottom=None, right=None, width=0.1)
            ),
            ButtonView(
                text="Play",
                callback=lambda: self.director.replace_scene(AttributeSelectionScene(game_context)),
                layout_options=LayoutOptions(top=0.5, height=0.2, left=0.4, right=None, bottom=None, width=0.1),
            ),
            ButtonView(
                text="Quit",
                callback=lambda: self.director.quit(),
                layout_options=LayoutOptions(top=0.5, height=0.2, left=0.5, right=None, bottom=None, width=0.1)
            )
        ]
        super().__init__(views)
