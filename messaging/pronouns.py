class Pronoun(object):
    MALE = ""
    FEMALE = ""
    NEUTER = ""
    PLAYER = ""

    def __init__(self, subject):
        self.subject = subject
        self.value = ""

    def format(self, context):
        subject = self.subject(context).value
        if hasattr(subject, 'gender'):
            gender = subject.gender.value
        else:
            gender = None

        if subject.player:
            self.value = self.PLAYER
        elif gender is None:
            self.value = self.NEUTER
        elif gender == "Male":
            self.value = self.MALE
        elif gender == "Female":
            self.value = self.FEMALE

        return self

    def __str__(self):
        return self.value


class He(Pronoun):
    MALE = "he"
    FEMALE = "she"
    NEUTER = "it"
    PLAYER = "you"


class Him(Pronoun):
    MALE = "him"
    FEMALE = "her"
    NEUTER = "it"
    PLAYER = "you"


class His(Pronoun):
    MALE = "his"
    FEMALE = "her"
    NEUTER = "its"
    PLAYER = "your"
