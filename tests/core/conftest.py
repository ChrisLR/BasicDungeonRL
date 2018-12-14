import pytest

from bflib.characters import classes, races, abilityscores
from bflib.items import Dagger
from bfgame.displaypriority import DisplayPriority
from bfgame.factories.character import CharacterFactory
from bfgame.factories.items import ItemFactory
from core.util.colors import Colors


@pytest.fixture
def sample_player():
    return CharacterFactory.create_new(
        ability_score_set=abilityscores.AbilityScoreSet.set_all(8),
        base_classes=(classes.Fighter, ),
        base_race=races.Human,
        symbol="@",
        fg_color=Colors.WHITE,
        bg_color=Colors.BLACK,
        display_priority=DisplayPriority.Player
    )


@pytest.fixture
def sample_weapon():
    return ItemFactory.create_new(Dagger)
