class EchoService(object):
    def __init__(self, game):
        self.game = game
        self.messages = []

    def _echo(self, message, context=None):
        if context:
            self.messages.append(message.do(context) + "\n")
        else:
            self.messages.append(message + "\n")

    def see(self, actor, message, context):
        if actor.player:
            return self._echo(message, context)

        player = self.game.player
        if player and player.vision.can_see_object(actor):
            self._echo(message, context)

    def system(self, message):
        self._echo(message)

    def player(self, actor, message, context=None):
        if actor.player:
            self._echo(message, context)

    def see_m(self, actor, target, actor_message, target_message, observer_message):
        """
        A simpler way to use see messages without context.
        """
        player = self.game.player
        if actor is player:
            return self._echo(actor_message)

        if player and player.vision.can_see_object(actor):
            if target is player:
                self._echo(target_message)
            else:
                self._echo(observer_message)
