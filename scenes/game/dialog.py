from bearlibterminal import terminal
from clubsandwich.ui import WindowView, LabelView, LayoutOptions

from core.ui import CoreUIScene


class DialogScene(CoreUIScene):
    covers_screen = False

    def __init__(self, game, actor, chat_target, **kwargs):
        self.game = game
        self.actor = actor
        self.chat_target = chat_target
        self.last_top = 0.2
        self.last_left = 0
        self.label_value_pairs = []
        self.reply_label = LabelView("")
        self.reply_label.layout_options.column_right(0.5)
        self.keyed_options = {}
        self._subviews = []
        self.dialog_tree = actor.talker.talk_to(chat_target)
        self.options = self.dialog_tree.get_options(actor)
        keys = (letter for letter in 'ABCDEFGHJKILMNOPQRSTUVWXYZ')
        self.create_multiple_label_value_pairs(
            ((next(keys), option) for option in self.options))

        self.option_view = WindowView(
            title="", subviews=self._subviews,
            layout_options=LayoutOptions.column_left(0.5)
        )
        self.reply_view = WindowView(
            title="", subviews=[self.reply_label],
            layout_options=LayoutOptions.column_right(0.5)
        )
        self.window_view = WindowView(
            title="Chatting with %s" % chat_target.name,
            subviews=[self.option_view, self.reply_view],
            layout_options=LayoutOptions.row_bottom(0.3)
        )
        self.end = False
        super().__init__(views=[self.window_view], **kwargs)

    def get_next_layout_pair(self):
        self.last_top += 0.1
        if self.last_top >= 0.8:
            self.last_top = 0.3
            self.last_left += 0.3
            if self.last_left > 0.9:
                raise Exception("Too many.")
        label = LayoutOptions(
            top=self.last_top,
            left=self.last_left,
            width=0.1, height=0.1,
            bottom=None, right=None
        )
        value = LayoutOptions(
            top=self.last_top,
            left=self.last_left + 0.1,
            width=0.1, height=0.1,
            bottom=None, right=None
        )

        return label, value

    def create_label_value_pair(self, label_text, value):
        label_layout, value_layout = self.get_next_layout_pair()
        label_view = LabelView(
            label_text,
            layout_options=label_layout,
        )
        current_value = value.ask_text
        value_view = LabelView(
            current_value,
            layout_options=value_layout,
        )
        ''
        self.keyed_options[label_text] = value
        self.label_value_pairs.append((label_view, value_view))
        self._subviews.append(label_view),
        self._subviews.append(value_view)

        return label_view, value_view

    def create_multiple_label_value_pairs(self, label_value_pairs):
        for label_value_pair in label_value_pairs:
            self.create_label_value_pair(*label_value_pair)

    def terminal_read(self, val):
        super().terminal_read(val)
        if self.end is True:
            self.game.director.pop_scene(self)
            return

        char = chr(terminal.state(terminal.TK_WCHAR)).upper()
        # TODO Display the NPC reply Here
        option = self.keyed_options.get(char)
        if option is not None:
            self.reply_label.text = option.reply_text
            # TODO Very not convenient, make this simpler
            self.options = self.actor.talker.say(self.dialog_tree, option)
            if self.options:
                keys = (letter for letter in 'ABCDEFGHJKILMNOPQRSTUVWXYZ')
                views = (view_pair for view_pair in self.label_value_pairs)
                for option in self.options:
                    key = next(keys)
                    view = next(views, None)
                    if view is None:
                        key_view, value_view = self.create_label_value_pair(key, option)
                        self.option_view.content_view.add_subviews([key_view, value_view])
                        self.option_view.content_view.layout_subviews()
                    else:
                        key_view, value_view = view
                    self.keyed_options[key] = option
                    value_view.text = option.ask_text
            else:
                self.option_view.content_view.remove_subviews(self._subviews)
                self.end = True
