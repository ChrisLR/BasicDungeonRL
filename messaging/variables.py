import abc


class MessageVariable(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, context):
        self.value = self.get_value(context)

    @abc.abstractmethod
    def get_value(self, context):
        pass

    def __str__(self):
        return self.value


class Attacker(MessageVariable):
    def get_value(self, context):
        self.value = context.attacker

    def __str__(self):
        if self.value.player:
            return "you"
        return self.value.name


class Defender(MessageVariable):
    def get_value(self, context):
        self.value = context.defender

    def __str__(self):
        if self.value.player:
            return "you"
        return self.value.name
