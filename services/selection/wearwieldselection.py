import functools

from clubsandwich.ui import UIScene, WindowView, LayoutOptions

from core.game.manager import game
from services.selection.base import Selection
from ui.views import KeyAssignedListView, SelectableButtonView


class WieldedWornSelection(Selection):
    def __init__(self, executor):
        super().__init__(executor)
        self.view = None

    def resolve(self):
        self.view = WieldedWornSelectionView(self)
        game.game_context.director.push_scene(self.view)


class WieldedWornSelectionView(UIScene):
    covers_screen = False

    def __init__(self, selection):
        self.selection = selection
        controls = [
            SelectableButtonView(
                target.name,
                functools.partial(self.select_object, value=target)
            )
            for target in self.selection.executor.equipment.get_all_items()
        ]
        super().__init__([
            WindowView(
                title="Select the item",
                subviews=[KeyAssignedListView(controls, value_column_width=64)],
                layout_options=LayoutOptions(width=0.5, left=0.3, height=0.9, right=None, bottom=None),
            )
        ])
        self.selections = []

    def select_object(self, value):
        self.selection.resolution = value,
        self.director.pop_scene()