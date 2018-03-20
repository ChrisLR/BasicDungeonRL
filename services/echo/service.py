from services.echo.functions import is_player


class EchoService(object):
    def __init__(self, game):
        self.game = game
        self.messages = []

    def _echo(self, message):
        self.messages.append(message + "\n")

    def see(self, actor, actor_message, observer_message):
        if is_player(actor):
            return self.player_echo(actor, actor_message)

        player = self.game.player
        if player and player.vision.can_see_object(actor):
            self._echo(observer_message)

    def system_echo(self, message):
        self._echo(message)

    def player_echo(self, actor, message):
        if is_player(actor):
            self._echo(message)
