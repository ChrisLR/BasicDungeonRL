class EchoService(object):
    def __init__(self, game):
        self.game = game
        self.messages = []

    def _echo(self, message, context=None):
        if context:
            self.messages.append(message.do(context))
        self.messages.append(message + "\n")

    def see(self, actor, message, context):
        if actor.player:
            return self._echo(message, context)

        player = self.game.player
        if player and player.vision.can_see_object(actor):
            self._echo(message, context)

    def system(self, message):
        self._echo(message)

    def player(self, actor, message, context):
        if actor.player:
            self._echo(message, context)
