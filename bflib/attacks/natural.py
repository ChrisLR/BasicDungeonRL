from bflib.attacks.base import NaturalAttack


class Bite(NaturalAttack):
    name = "Bite"


class Claw(NaturalAttack):
    name = "Claw"


class Crush(NaturalAttack):
    """ Crush requires Grapple Hold"""
    name = "Crush"


class ConfusionBySwarm(NaturalAttack):
    name = "Confuse"


class Gaze(NaturalAttack):
    name = "Gaze"


class Headbutt(NaturalAttack):
    name = "Headbutt"


class Hoof(NaturalAttack):
    name = "Hoof"


class Sting(NaturalAttack):
    name = "Sting"
