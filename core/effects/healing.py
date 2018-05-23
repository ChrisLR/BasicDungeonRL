from bflib import effects
from bflib.dice import D6
from core.contexts import Action
from core.effects.base import Effect
from messaging import StringBuilder, Actor, Verb


class Healing(Effect):
    name = "Healing"

    base_effect = effects.Healing
    """
    Every round, recover health
    """
    def __init__(self, duration, power=None, dice=D6(1)):
        super().__init__(duration, power, dice)

    def on_start(self, game_object):
        """
        Show a message,
        :param game_object:
        :return:
        """
        context = Action(game_object, None)
        message = StringBuilder(Actor, Verb("start", Actor),  "healing!")

        game_object.game.echo.see(
            actor=game_object,
            message=message,
            context=context,
        )

    def update(self, game_object):
        """
        At Each Update it deals damage to the game_object and shows a message
        :param game_object:
        :return:
        """
        super().update(game_object)
        health = self.dice.roll_total()
        context = Action(game_object, None)
        message = StringBuilder(Actor, Verb("recover", Actor), "%s health!" % health)

        game_object.game.echo.see(
            actor=game_object,
            message=message,
            context=context,
        )

        game_object.health.restore_health(health)

    def on_finish(self, game_object):
        context = Action(game_object, None)
        message = StringBuilder(Actor, Verb("is", Actor), "no longer healing.")
        game_object.game.echo.see(
            actor=game_object,
            message=message,
            context=context,
        )
