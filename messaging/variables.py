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
        return context.attacker

    def __str__(self):
        if self.value.player:
            return "you"
        return self.value.name


class Ammunition(MessageVariable):
    def get_value(self, context):
        return context.ammunition

    def __str__(self):
        return self.value.name


class Defender(MessageVariable):
    def get_value(self, context):
        return context.defender

    def __str__(self):
        if self.value.player:
            return "you"
        return self.value.name


class AttackerWeapon(MessageVariable):
    def get_value(self, context):
        return context.attacker_weapon

    def __str__(self):
        return self.value.name


class Actor(MessageVariable):
    def get_value(self, context):
        return context.actor

    def __str__(self):
        if self.value.player:
            return "you"
        return self.value.name


class Target(MessageVariable):
    def get_value(self, context):
        return context.target

    def __str__(self):
        if self.value.player:
            return "you"
        return self.value.name


class TargetOne(Target):
    def get_value(self, context):
        return context.target_one


class TargetTwo(Target):
    def get_value(self, context):
        return context.target_two
