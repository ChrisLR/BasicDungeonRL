from core.threatlevels import ThreatLevel


class BodyPart(object):
    NAME = ""
    abilities = tuple()
    item_slots = tuple()
    threat_level = None
    base_relative_size = None

    def __init__(self, name=None, relative_size=None):
        self.parent = None
        self.attached_children = []
        self.embedded_children = []
        self.name = name if name is not None else self.NAME
        self.relative_size = (relative_size if relative_size is not None
                              else self.base_relative_size)

    def attach(self, *bodyparts):
        self.attached_children.extend(bodyparts)
        for bodypart in bodyparts:
            bodypart.parent = self

    def detach(self, bodypart):
        self.attached_children.remove(bodypart)
        bodypart.parent = None

    def insert(self, *bodyparts):
        self.embedded_children.extend(bodyparts)
        for bodypart in bodyparts:
            bodypart.parent = self

    def remove(self, bodypart):
        self.embedded_children.remove(bodypart)
        bodypart.parent = None

    def get_all_descendants(self):
        descendants = set()
        descendants.update(self.attached_children)
        descendants.update(self.embedded_children)
        for child in self.attached_children:
            descendants.update(child.get_all_descendants())

        return descendants


class Head(BodyPart):
    NAME = "head"
    base_relative_size = 25
    threat_level = ThreatLevel.Major


class Neck(BodyPart):
    NAME = "neck"
    base_relative_size = 10
    threat_level = ThreatLevel.Critical


class Torso(BodyPart):
    NAME = "torso"
    base_relative_size = 50
    threat_level = ThreatLevel.Major


class Arm(BodyPart):
    NAME = "arm"
    base_relative_size = 25
    threat_level = ThreatLevel.Major


class Leg(BodyPart):
    NAME = "leg"
    base_relative_size = 25
    threat_level = ThreatLevel.Major


class Hand(BodyPart):
    NAME = "hand"
    base_relative_size = 10
    threat_level = ThreatLevel.Minor


class Foot(BodyPart):
    NAME = "foot"
    base_relative_size = 10
    threat_level = ThreatLevel.Minor


class Eye(BodyPart):
    NAME = "eye"
    base_relative_size = 5
    threat_level = ThreatLevel.Critical


class Ear(BodyPart):
    NAME = "ear"
    base_relative_size = 5
    threat_level = ThreatLevel.Minor


class Mouth(BodyPart):
    NAME = "mouth"
    base_relative_size = 5
    threat_level = ThreatLevel.Minor


class Nose(BodyPart):
    NAME = "nose"
    base_relative_size = 5
    threat_level = ThreatLevel.Minor


class Brain(BodyPart):
    NAME = "brain"
    base_relative_size = 15
    threat_level = ThreatLevel.Fatal


class Heart(BodyPart):
    NAME = "heart"
    base_relative_size = 25
    threat_level = ThreatLevel.Fatal


class Lungs(BodyPart):
    NAME = "lungs"
    base_relative_size = 25
    threat_level = ThreatLevel.Fatal


class Teeth(BodyPart):
    NAME = "teeth"
    base_relative_size = 5
    threat_level = ThreatLevel.Major


class Muzzle(BodyPart):
    NAME = "Muzzle"
    base_relative_size = 15
    threat_level = ThreatLevel.Major


class Fangs(BodyPart):
    NAME = "Fangs"
    base_relative_size = 5
    threat_level = ThreatLevel.Major


class Tail(BodyPart):
    NAME = "Tail"
    base_relative_size = 25
    threat_level = ThreatLevel.Minor
