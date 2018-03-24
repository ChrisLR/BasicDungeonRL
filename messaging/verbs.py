class Verb(object):
    def __init__(self, verb, subject):
        self.verb = verb
        self.subject = subject
        self.value = ""

    def format(self, context):
        subject = self.subject.get_value(context)
        if subject.player:
            self.value = self.verb
        else:
            self.value = third_personify(self.verb)

    def __str__(self):
        return self.value


mapping = {
    "y": lambda verb: verb[:-1] + "ies",
    "s": lambda verb: verb + "es",
    "z": lambda verb: verb + "es",
    "h": lambda verb: verb + "es",
    "x": lambda verb: verb + "es",
    "o": lambda verb: verb + "es",
}


def third_personify(verb):
    last_letter = verb[-1]
    result = mapping.get(last_letter, lambda v: v + "s")

    return result(verb)
