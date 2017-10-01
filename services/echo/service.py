class EchoService(object):
    def __init__(self):
        self.console = None
        self.game_context = None

    def echo(self, message):
        self.console.add_lines(message + "\n")


echo_service = EchoService()
