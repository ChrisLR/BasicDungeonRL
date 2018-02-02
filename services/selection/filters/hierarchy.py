import collections
import functools

from bearlibterminal import terminal
from clubsandwich.ui import ButtonView, UIScene, WindowView, LayoutOptions

from core.game.manager import game
from services.selection.filters.base import SelectionFilter
from ui.views import KeyAssignedListView, SelectableButtonView


class HierarchyFilterView(UIScene):
    covers_screen = False

    def __init__(self, host_filter, hierarchy):
        self.hierarchy = hierarchy
        self.button_controls_list = []
        self._recursive_create_buttons(hierarchy)
        self.button_controls = collections.OrderedDict(self.button_controls_list)
        super().__init__([
            WindowView(
                "",
                subviews=[
                    KeyAssignedListView(
                        self.button_controls.values(),
                        value_column_width=max(len(value.text) + 5 for value in self.button_controls.values()),
                        layout_options=LayoutOptions.column_left(0.9)),
                ],
                layout_options=LayoutOptions(width=0.5, left=0.3, height=0.9, right=None, bottom=None),
            ),
            ButtonView("Finish", self.finish, layout_options=LayoutOptions.row_bottom(0.2)),
        ])
        self.host_filter = host_filter
        self.selections = []

    def _recursive_create_buttons(self, hierarchy, depth=0):
        """
        This creates buttons recursively for a hierarchy.
        :type hierarchy: dict
        :param hierarchy:
        """
        for parent, children in hierarchy.items():
            button_control = self._create_selectable_button(parent, depth)
            self.button_controls_list.append((parent, button_control))
            if isinstance(children, dict):
                self._recursive_create_buttons(children, depth + 1)
            elif isinstance(children, list):
                for child in children:
                    button_control = self._create_selectable_button(child, depth + 1)
                    self.button_controls_list.append((child, button_control))

    def _create_selectable_button(self, game_object, depth=0):
        return SelectableButtonView(
            "{}{}".format("-" * depth, game_object.name),
            functools.partial(self.select_object, value=game_object),
            align_horz='left'
        )

    def finish(self):
        self.host_filter.resolution = self.selections
        self.director.pop_scene()

    def select_object(self, value):
        if value in self.selections:
            self.button_controls[value].deselect()
            self.selections.remove(value)
        else:
            self.button_controls[value].select()
            self.selections.append(value)

    def terminal_read(self, val):
        super().terminal_read(val)
        if val == terminal.TK_ESCAPE:
            self.host_filter.canceled = True
            self.director.pop_scene()


class SingleHierarchyFilterView(HierarchyFilterView):
    def select_object(self, value):
        self.finish()
        self.selections = [value]


class Hierarchy(SelectionFilter):
    """
    A Selection Filter that includes a hierarchy based on containers/contained
    """
    view_type = HierarchyFilterView

    def __init__(self):
        super().__init__()
        self.view = None

    def filter(self, targets):
        item_hierarchy = {}
        for target in targets:
            inventory = target.inventory
            if inventory:
                item_hierarchy[target] = inventory.get_item_hierarchy()
            elif target.container:
                container = target.container
                if container:
                    if target.openable:
                        if not target.openable.closed:
                            item_hierarchy[target] = container.items_held
                    else:
                        item_hierarchy[target] = container.items_held
            else:
                item_hierarchy[target] = []

        self.view = self.view_type(self, item_hierarchy)
        game.game_context.director.push_scene(self.view)


class SingleHierarchy(Hierarchy):
    view_type = SingleHierarchyFilterView
