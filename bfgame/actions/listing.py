from bfgame.actions.addclass import AddClass
from bfgame.actions.bump import Bump
from bfgame.actions.close import Close
from bfgame.actions.climb import ClimbUp, ClimbDown
from bfgame.actions.drop import Drop
from bfgame.actions.eat import Eat
from bfgame.actions.fire import Fire
from bfgame.actions.get import Get
from bfgame.actions.look import Look
from bfgame.actions.move import WalkE, WalkN, WalkNE, WalkNW, WalkS, WalkSE, WalkSW, WalkW
from bfgame.actions.open import Open
from bfgame.actions.put import Put
from bfgame.actions.remove import Remove
from bfgame.actions.showskills import ShowSkills
from bfgame.actions.useability import UseAbility
from bfgame.actions.wear import Wear
from bfgame.actions.wield import Wield
from bfgame.actions.jump import Jump


action_listing = {
    AddClass,
    Bump,
    Close,
    ClimbUp,
    ClimbDown,
    Drop,
    Eat,
    Get,
    Fire,
    Look,
    Jump,
    WalkE,
    WalkN,
    WalkNE,
    WalkNW,
    WalkS,
    WalkSE,
    WalkSW,
    WalkW,
    Open,
    Put,
    Remove,
    ShowSkills,
    Wear,
    Wield,
    UseAbility
}

action_mapping = {
    action.name: action for action in action_listing
}


def get_by_name(action_name):
    return action_mapping.get(action_name)
