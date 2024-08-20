class Head:
    def __init__(self):
        pass


class Hand:
    def __init__(self):
        pass


class Feet:
    def __init__(self):
        pass


class Arm:
    def __init__(self, hand):
        self.hand = hand


class Leg:
    def __init__(self, foot):
        self.foot = foot


class Torso:
    def __init__(self, right_arm, left_arm, head, right_leg, left_leg):
        self.right_arm = right_arm
        self.left_arm = left_arm
        self.head = head
        self.right_leg = right_leg
        self.left_leg = left_leg


class Human:
    def __init__(self):
        head = Head()

        right_hand = Hand()
        right_arm = Arm(right_hand)

        left_hand = Hand()
        left_arm = Arm(left_hand)

        right_foot = Feet()
        right_leg  = Leg(right_foot)

        left_foot = Feet()
        left_leg = Leg(left_foot)

        self.body = Torso(right_arm, left_arm, head, right_leg, left_leg)


person = Human()

print(person.body.left_arm.hand)
print(person.body.head)
print(person.body.right_leg.foot)

