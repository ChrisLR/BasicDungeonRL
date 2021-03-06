from bflib import attacks, dice
from core import materials, bodyparts
from core.bodies import Body
from core.bodies import Blood


class HumanoidBody(Body):
    name = "Humanoid"
    base_height = 5
    base_weight = 150

    template_blood = Blood
    template_structural_material = materials.Bone
    template_inner_material = materials.Flesh
    template_outer_material = materials.Skin

    def __init__(self):
        head = bodyparts.Head()
        brain = bodyparts.Brain()
        left_eye = bodyparts.Eye("Left Eye")
        right_eye = bodyparts.Eye("Right Eye")
        left_ear = bodyparts.Ear("Left Ear")
        right_ear = bodyparts.Ear("Right Ear")
        neck = bodyparts.Neck()
        torso = bodyparts.Torso()
        heart = bodyparts.Heart()
        left_arm = bodyparts.Arm("Left Arm")
        left_hand = bodyparts.Hand("Left Hand")
        right_arm = bodyparts.Arm("Right Arm")
        right_hand = bodyparts.Hand("Right Hand")
        left_leg = bodyparts.Leg("Left Leg")
        left_foot = bodyparts.Foot("Left Foot")
        right_leg = bodyparts.Leg("Right Leg")
        right_foot = bodyparts.Foot("Right Foot")

        head.attach(left_eye, right_eye, left_ear, right_ear, neck)
        head.insert(brain)
        neck.attach(torso)
        torso.attach(left_arm, right_arm, left_leg, right_leg)
        torso.insert(heart)
        left_arm.attach(left_hand)
        right_arm.attach(right_hand)
        left_leg.attach(left_foot)
        right_leg.attach(right_foot)

        super().__init__(head.get_all_descendants())
        punch_attack = attacks.AttackSet(attacks.Punch(dice.D4(1)))
        self.bind_attack(punch_attack, (left_arm, left_hand))
        self.bind_attack(punch_attack, (right_arm, right_hand))

        kick_attack = attacks.AttackSet(attacks.Kick(dice.D4(1)))
        self.bind_attack(kick_attack, (left_leg, left_foot))
        self.bind_attack(kick_attack, (right_leg, right_foot))
