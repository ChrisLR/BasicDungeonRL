from bearlibterminal import terminal

from core import actions

lowercase_mapping = {
    terminal.TK_KP_7: actions.WalkNW,
    terminal.TK_KP_8: actions.WalkN,
    terminal.TK_KP_9: actions.WalkNE,
    terminal.TK_KP_6: actions.WalkE,
    terminal.TK_KP_3: actions.WalkSE,
    terminal.TK_KP_2: actions.WalkS,
    terminal.TK_KP_1: actions.WalkSW,
    terminal.TK_KP_4: actions.WalkW,
    terminal.TK_O: actions.Open,
    terminal.TK_C: actions.Close,
    terminal.TK_G: actions.Get,
    terminal.TK_W: actions.Wear,
    terminal.TK_R: actions.Remove,
    terminal.TK_D: actions.Drop,
    terminal.TK_X: actions.Look,
    terminal.TK_P: actions.Put
}

uppercase_mapping = {
    terminal.TK_W: actions.Wield,
}
