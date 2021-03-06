from bfgame.actions.addclass import AddClass
from bfgame.actions.climb import ClimbUp, ClimbDown
from bfgame.actions.fire import Fire
from bfgame.actions.jump import Jump
from bfgame.actions.showskills import ShowSkills
from bfgame.actions.useability import UseAbility
from core.actions.bump import Bump
from core.actions.close import Close
from core.actions.drop import Drop
from core.actions.eat import Eat
from core.actions.get import Get
from core.actions.look import Look
from core.actions.move import WalkE, WalkN, WalkNE, WalkNW, WalkS, WalkSE, WalkSW, WalkW
from core.actions.open import Open
from core.actions.put import Put
from core.actions.remove import Remove
from core.actions.wear import Wear
from core.actions.wield import Wield

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
