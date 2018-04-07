from core.bodies.base import Body
from core.bodies.blood import Blood
from core import materials, bodyparts


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
