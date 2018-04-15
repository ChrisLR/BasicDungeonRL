from messaging.variables import MessageVariable
from messaging.verbs import Verb
from messaging.pronouns import Pronoun


class StringBuilder(object):
    def __init__(self, *args):
        self.args = list(args)

    def do(self, context):
        p_args = []
        for arg in self.args:
            if isinstance(arg, str):
                p_args.append(arg)
            elif isinstance(arg, Verb):
                p_args.append(str(arg.format(context)))
            elif isinstance(arg, Pronoun):
                p_args.append(str(arg.format(context)))
            elif issubclass(arg, MessageVariable):
                p_args.append(str(arg(context)))

        partial_result = " ".join(p_args).capitalize()

        return partial_result.replace(" '", "'").replace(" .", ".")

    def __add__(self, other):
        args = self.args.copy()
        args.append(other)

        return StringBuilder(*args)
