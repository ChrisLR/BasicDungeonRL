from bfgame.abilities.hide import Hide
from bfgame.abilities.immolation import Immolation, InfiniteImmolation, SmallImmolation
from bfgame.abilities.movesilently import MoveSilently
from bfgame.abilities.openlock import OpenLock
from bfgame.abilities.pickpocket import PickPocket
from bfgame.abilities.removetraps import RemoveTraps


ability_listing = {
    Hide,
    Immolation,
    InfiniteImmolation,
    SmallImmolation,
    MoveSilently,
    OpenLock,
    PickPocket,
    RemoveTraps,
}
ability_mapping = {
    ability.name: ability for ability in ability_listing
}


def get_by_name(action_name):
    return ability_mapping.get(action_name)
