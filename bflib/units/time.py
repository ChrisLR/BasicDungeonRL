import abc

from bflib.units.base import Unit


class TimeUnit(Unit):
    __metaclass__ = abc.ABCMeta
    value_to_seconds = 0

    def to_seconds(self):
        return self.value * self.value_to_seconds

    def to_game_turns(self):
        return GameTurn.from_seconds(self.to_seconds())

    def to_combat_rounds(self):
        return CombatRound.from_seconds(self.to_seconds())

    @classmethod
    def from_seconds(cls, seconds):
        return CombatRound(round(seconds / cls.value_to_seconds))


class GameTurn(TimeUnit):
    value_to_seconds = 600


class CombatRound(TimeUnit):
    value_to_seconds = 10
