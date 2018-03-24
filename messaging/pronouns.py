class Pronoun(object):
    MALE = ""
    FEMALE = ""
    NEUTER = ""

    def __init__(self, subject):
        self.subject = subject
        self.value = ""

    def format(self, context):
        subject = self.subject.get_value(context)
        gender = subject.gender
        if gender is None:
            self.value = self.NEUTER
        elif gender == "Male":
            self.value = self.MALE
        elif gender == "Female":
            self.value = self.FEMALE

    def __str__(self):
        return self.value


class He(Pronoun):
    MALE = "he"
    FEMALE = "she"
    NEUTER = "it"


class Him(Pronoun):
    MALE = "him"
    FEMALE = "her"
    NEUTER = "it"


class His(Pronoun):
    MALE = "his"
    FEMALE = "her"
    NEUTER = "its"
