from bfgame.ai.behaviors.base import Behavior


class Wait(Behavior):
    def __init__(self, host, turns=1):
        """
        :param host: Behavior Executor
        :param turns: How many turns to wait, can be a dice, None or int
        """
        super().__init__(host)
        self.turns = 0
        self.max_turns = int(turns) if turns is not None else None
        self.finished = False

    def execute(self):
        if not self.max_turns:
            return

        if self.turns < self.max_turns:
            self.turns += 1
        else:
            self.finished = True
