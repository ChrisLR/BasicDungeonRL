from services.echo.functions import is_player


class EchoService(object):
    def __init__(self):
        self.messages = []

    def echo(self, message):
        self.messages.append(message + "\n")


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
        from core.game.manager import game
        player = game.game_context.player
        if player:
            if player.vision.can_see_object(actor):
                system_echo(observer_message)
