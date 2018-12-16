import abc

from bflib.units.time import TimeUnit, CombatRound


class Effect(object):
    __metaclass__ = abc.ABCMeta
    name = ""
    base_effect = None

    def __init__(self, duration, power=1, dice=None):
        """
        :param duration: Duration of the effect, None is infinite.
        :type duration: TimeUnit
        :param dice: Dice instance if needed.
        :param power: Arbitrary multiplier for an effect.
        """
        self.dice = dice
        self.duration = duration.to_seconds() if duration is not None else None
        self.elapsed = 0
        self.power = power

    @property
    def finished(self):
        if self.duration is None:
            return False
        return self.elapsed >= self.duration

    @abc.abstractmethod
    def on_start(self, game_object):
        pass

    def update(self, game_object):
        self.elapsed += CombatRound.value_to_seconds

    @abc.abstractmethod
    def on_finish(self, game_object):
        pass
