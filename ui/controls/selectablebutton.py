from clubsandwich.ui.misc_views import ButtonView


class SelectableButtonView(ButtonView):
    def __init__(self, text, callback, align_horz='center', align_vert='center',
                 color_fg='#ffffff', color_bg='#000000', size=None, selected_color='#efff14', *args, **kwargs):
        super().__init__(text, callback, align_horz, align_vert,
                         color_fg, color_bg, size, *args, **kwargs)
        self._selected = False
        self.selected_color = selected_color
        self.responder = False

    def select(self):
        self._selected = True
        if self.responder:
            self.label_view.color_bg = self.selected_color
        else:
            self.label_view.color_fg = self.selected_color

    def deselect(self):
        self._selected = False
        if self.responder:
            self.label_view.color_bg = self.color_fg
        else:
            self.label_view.color_fg = self.color_fg

    def did_become_first_responder(self):
        self.responder = True
        if self._selected:
            self.label_view.color_bg = self.selected_color
            self.label_view.color_fg = self.color_bg
        else:
            super().did_become_first_responder()

    def did_resign_first_responder(self):
        self.responder = False
        if self._selected:
            self.label_view.color_fg = self.selected_color
            self.label_view.color_bg = self.color_bg
        else:
            super().did_resign_first_responder()
