from bflib import dice
from bfgame import contexts
from bfgame.effects.base import Effect
from core.messaging import StringBuilder, Actor, Verb


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
        context = contexts.Action(game_object, None)
        message = StringBuilder(Actor, Verb("are", Actor), "on fire!")
        game_object.game.echo.see(game_object, message, context)

    def update(self, game_object):
        """
        At Each Update it deals damage to the game_object and shows a message
        :param game_object:
        :return:
        """
        super().update(game_object)
        damage = dice.D6(self.power).roll_total()
        # TODO This should be elemental Fire Damage.
        context = contexts.Action(game_object, None)
        message = StringBuilder(Actor, Verb("burn", Actor), "for %s damage!" % damage)
        game_object.game.echo.see(game_object, message, context)
        game_object.health.take_damage(damage)

    def on_finish(self, game_object):
        context = contexts.Action(game_object, None)
        message = StringBuilder(Actor, Verb("are", Actor), "no longer burning.")
        game_object.game.echo.see(game_object, message, context)
