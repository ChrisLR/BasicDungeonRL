from services.echo.functions import is_player


class EchoService(object):
    def __init__(self):
        self.console = None
        self.game_context = None

    def echo(self, message):
        if self.console:
            self.console.add_lines(message + "\n")


echo_service = EchoService()


def system_echo(message):
    echo_service.echo(message)


def player_echo(actor, message):
    if is_player(actor):
        echo_service.echo(message)


def see(actor, actor_message, observer_message):
    if is_player(actor):
        player_echo(actor, actor_message)
    else:
        player = echo_service.game_context.player
        if player.vision.can_see_object(actor):
            system_echo(observer_message)
