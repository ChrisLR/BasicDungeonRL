from bflib import dice
from core.effects.base import Effect
from services import echo


class Burning(Effect):
    name = "Burning"
    """
    Every round, deals Fire damage to the Host
    """
    def on_start(self, game_object):
        """
        Show a message,
        :param game_object:
        :return:
        """
        # You are on fire!
        if echo.is_player(game_object):
            echo.echo_service.echo("You are on fire!")
        else:
            echo.echo_service.echo("{} is on fire!".format(game_object.name))

    def update(self, game_object):
        """
        At Each Update it deals damage to the game_object and shows a message
        :param game_object:
        :return:
        """
        super().update(game_object)
        damage = dice.D6(self.power).roll()
        # TODO This should be elemental Fire Damage.
        game_object.health.take_damage(damage)
        if echo.is_player(game_object):
            echo.echo_service.echo("You burn for {} damage!".format(damage))
        else:
            echo.echo_service.echo("{} burns for {} damage!".format(game_object.name, damage))

    def on_finish(self, game_object):
        if echo.is_player(game_object):
            echo.echo_service.echo("You are no longer burning.")
        else:
            echo.echo_service.echo("{} is no longer burning!".format(game_object.name))