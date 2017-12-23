from clubsandwich.ui import RectView, LabelView, LayoutOptions


class HudView(RectView):
    def __init__(self, game_context, **kwargs):
        self.game_context = game_context
        self.last_top = 0
        self.last_left = 0
        self.label_value_pairs = []
        self._subviews = []
        player = game_context.player
        player_stats = player.stats
        self.create_multiple_label_value_pairs(
            ('Name:', lambda: player.name),
            ('Strength:', lambda: str(player_stats.strength)),
            ('Dexterity:', lambda: str(player_stats.dexterity)),
            ('Constitution:', lambda: str(player_stats.constitution)),
            ('Intelligence:', lambda: str(player_stats.intelligence)),
            ('Wisdom:', lambda: str(player_stats.wisdom)),
            ('Charisma:', lambda: str(player_stats.charisma)),
            ('Health:', lambda: str(player.health.current))
        )

        super().__init__(
            subviews=self._subviews, fill=True, **kwargs
        )

    def draw(self, ctx):
        for label_value_pair in self.label_value_pairs:
            _, value_view = label_value_pair
            updated_value = value_view.update_value()
            value_view.text = updated_value
        super().draw(ctx)

    def get_next_layout_pair(self):
        self.last_top += 0.1
        if self.last_top >= 0.8:
            self.last_top = 0.1
            self.last_left += 0.2
            if self.last_left > 0.9:
                raise Exception("Too many.")
        label = LayoutOptions(
            top=self.last_top, left=self.last_left,
            width=0.2, height=0.1,
            bottom=None, right=None
        )
        value = LayoutOptions(
            top=self.last_top,
            left=self.last_left + 0.1,
            width=0.2, height=0.1,
            bottom=None, right=None
        )

        return label, value

    def create_label_value_pair(self, label_text, value_lambda):
        label_layout, value_layout = self.get_next_layout_pair()
        label_view = LabelView(
            label_text,
            layout_options=label_layout,
        )
        current_value = value_lambda()
        value_view = LabelView(
            current_value,
            layout_options=value_layout,
        )
        setattr(value_view, 'update_value', value_lambda)
        self.label_value_pairs.append((label_view, value_view))
        self._subviews.append(label_view),
        self._subviews.append(value_view)

    def create_multiple_label_value_pairs(self, *label_value_pairs):
        for label_value_pair in label_value_pairs:
            self.create_label_value_pair(*label_value_pair)
