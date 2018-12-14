from bearlibterminal import terminal


class ActionMapping(object):
    def __init__(self, game):
        self.game = game
        self.lowercase = {
            terminal.TK_KP_7: "walk_nw",
            terminal.TK_KP_8: "walk_n",
            terminal.TK_KP_9: "walk_ne",
            terminal.TK_KP_6: "walk_e",
            terminal.TK_KP_3: "walk_se",
            terminal.TK_KP_2: "walk_s",
            terminal.TK_KP_1: "walk_sw",
            terminal.TK_KP_4: "walk_w",
            terminal.TK_E: "eat",
            terminal.TK_O: "open",
            terminal.TK_C: "close",
            terminal.TK_G: "get",
            terminal.TK_W: "wear",
            terminal.TK_R: "remove",
            terminal.TK_D: "drop",
            terminal.TK_X: "look",
            terminal.TK_P: "put",
            terminal.TK_A: "use_ability",
            terminal.TK_F: "fire",
            terminal.TK_J: "jump",
            terminal.TK_KP_PLUS: "climb_up",
            terminal.TK_KP_MINUS: "climb_down",
        }
        self.uppercase = {
            terminal.TK_W: "wield",
            terminal.TK_S: "show_skills"
        }

    def get_lowercase(self, key):
        name = self.lowercase.get(key)
        return self.game.actions.get_action_by_name(name)

    def get_uppercase(self, key):
        name = self.uppercase.get(key)
        return self.game.actions.get_action_by_name(name)
