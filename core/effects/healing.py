from bflib.dice import D6
from bflib import effects
from core.effects.base import Effect
from services import echo


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
        # You are on fire!
        if echo.is_player(game_object):
            echo.echo_service.echo("You are healing!")
        else:
            echo.echo_service.echo("{} is healing!".format(game_object.name))

    def update(self, game_object):
        """
        At Each Update it deals damage to the game_object and shows a message
        :param game_object:
        :return:
        """
        super().update(game_object)
        health = self.dice.roll()

        if echo.is_player(game_object):
            echo.echo_service.echo("You recover {} health.".format(health))
        else:
            echo.echo_service.echo("{} recovers {} health.".format(game_object.name, health))
        game_object.health.restore_health(health)

    def on_finish(self, game_object):
        if echo.is_player(game_object):
            echo.echo_service.echo("You are no longer healing.")
        else:
            echo.echo_service.echo("{} is no longer healing.".format(game_object.name))
