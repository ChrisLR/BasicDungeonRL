from clubsandwich.ui import LayoutOptions
from core.ui import CoreUIScene
from clubsandwich.ui.misc_views import LabelView, ButtonView


class MainMenuScene(CoreUIScene):
    ID = "MainMenu"

    def __init__(self, game):
        self.game = game
        self.covers_screen = True
        self.manager = None
        views = [
            LabelView(
                text="Placeholder Text for BasicDungeon",
                layout_options=LayoutOptions(top=0.4, height=0.1, left=None, bottom=None, right=None, width=0.1)
            ),
            ButtonView(
                text="Play",
                callback=self.finish,
                layout_options=LayoutOptions(top=0.5, height=0.2, left=0.4, right=None, bottom=None, width=0.1),
            ),
            ButtonView(
                text="Quit",
                callback=lambda: self.director.quit(),
                layout_options=LayoutOptions(top=0.5, height=0.2, left=0.5, right=None, bottom=None, width=0.1)
            )
        ]
        super().__init__(views)

    def finish(self):
        self.manager.next()
