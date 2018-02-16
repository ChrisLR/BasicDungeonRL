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
        echo.see(
            actor=game_object,
            actor_message="You are on fire!",
            observer_message="{} is on fire!".format(game_object.name),
        )

    def update(self, game_object):
        """
        At Each Update it deals damage to the game_object and shows a message
        :param game_object:
        :return:
        """
        super().update(game_object)
        damage = dice.D6(self.power).roll()
        # TODO This should be elemental Fire Damage.
        echo.see(
            actor=game_object,
            actor_message="You burn for {} damage!".format(damage),
            observer_message="{} burns for {} damage!".format(
                game_object.name, damage
            ),
        )

        game_object.health.take_damage(damage)

    def on_finish(self, game_object):
        echo.see(
            actor=game_object,
            actor_message="You are no longer burning.",
            observer_message="{} is no longer burning.".format(
                game_object.name
            ),
        )
