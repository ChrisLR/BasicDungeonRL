from core.components import listing, Component


@listing.register
class Dialog(Component):
    NAME = "dialog"
    __slots__ = ["mapping"]

    def __init__(self, dialog_tree):
        super().__init__()
        self.dialog_tree = dialog_tree

    def copy(self):
        return Dialog(self.dialog_tree)


class Talker(Component):
    NAME = "talker"
    __slots__ = ["progress"]

    def __init__(self):
        super().__init__()
        self._progress = {}

    def talk_to(self, game_object):
        dialog = game_object.dialog
        if dialog:
            return dialog.get_choices(self.host)

    def say(self, dialog_id, key):
        self._progress[dialog_id] = key
