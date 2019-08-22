from core.components import listing, Component


@listing.register
class Dialog(Component):
    NAME = "dialog"
    __slots__ = ["mapping"]

    def __init__(self, dialog_tree):
        super().__init__()
        self.dialog_tree = dialog_tree

    def get_options(self, talker, progress_id=None):
        return self.dialog_tree.get_options(talker, progress_id)

    def copy(self):
        return Dialog(self.dialog_tree)


@listing.register
class Talker(Component):
    NAME = "talker"
    __slots__ = ["progress"]

    def __init__(self):
        super().__init__()
        self._progress = {}

    def talk_to(self, game_object):
        dialog = game_object.dialog
        if dialog:
            return dialog.dialog_tree

    def say(self, dialog_tree, key):
        self._progress[dialog_tree.dialog_id] = key
        return dialog_tree.get_options(self.host, key)


