from bearlibterminal import terminal


class ActionMapping(object):
    def __init__(self, game):
        self.game = game
        self.lowercase = {
            terminal.TK_KP_7: game.actions.get_action_by_name("walk_nw"),
            terminal.TK_KP_8: game.actions.get_action_by_name("walk_n"),
            terminal.TK_KP_9: game.actions.get_action_by_name("walk_ne"),
            terminal.TK_KP_6: game.actions.get_action_by_name("walk_e"),
            terminal.TK_KP_3: game.actions.get_action_by_name("walk_se"),
            terminal.TK_KP_2: game.actions.get_action_by_name("walk_s"),
            terminal.TK_KP_1: game.actions.get_action_by_name("walk_sw"),
            terminal.TK_KP_4: game.actions.get_action_by_name("walk_w"),
            terminal.TK_E: game.actions.get_action_by_name("eat"),
            terminal.TK_O: game.actions.get_action_by_name("open"),
            terminal.TK_C: game.actions.get_action_by_name("close"),
            terminal.TK_G: game.actions.get_action_by_name("get"),
            terminal.TK_W: game.actions.get_action_by_name("wear"),
            terminal.TK_R: game.actions.get_action_by_name("remove"),
            terminal.TK_D: game.actions.get_action_by_name("drop"),
            terminal.TK_X: game.actions.get_action_by_name("look"),
            terminal.TK_P: game.actions.get_action_by_name("put"),
        }
        self.uppercase_mapping = {
            terminal.TK_W: game.actions.get_action_by_name("wield"),
        }
