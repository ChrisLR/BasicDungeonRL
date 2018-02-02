from bearlibterminal import terminal
from clubsandwich.ui import SettingsListView


class KeyAssignedListView(SettingsListView):
    CHARACTER_SET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!\"#$%?&*()_+^:'.|{}[]@"

    def __init__(self, value_controls, value_column_width=20, *args, **kwargs):
        symbols = (symbol for symbol in self.CHARACTER_SET)
        label_control_pairs = []
        for value_control in value_controls:
            label_control_pairs.append((next(symbols, " "), value_control))

        super().__init__(label_control_pairs, value_column_width=value_column_width, *args, **kwargs)

    def terminal_read(self, val):
        super().terminal_read(val)
        char = chr(terminal.state(terminal.TK_WCHAR))
        label_index = next((index for index, label in enumerate(self.labels)
                            if label.text == char), None)
        if label_index is not None:
            self.first_responder_container_view.set_first_responder(
                self.values[label_index])
