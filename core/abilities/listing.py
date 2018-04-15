from core.abilities.hide import Hide
from core.abilities.immolation import Immolation, InfiniteImmolation, SmallImmolation
from core.abilities.movesilently import MoveSilently
from core.abilities.openlock import OpenLock
from core.abilities.pickpocket import PickPocket
from core.abilities.removetraps import RemoveTraps


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
