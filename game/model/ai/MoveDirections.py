from game.lib.Random import Random


class MoveDirection:

    def __init__(self, name):
        self.name = name
        self.opposite = None
        self.applyInputData = None


class MoveDirections:

    stay = MoveDirection("stay")
    forward = MoveDirection("forward")
    backward = MoveDirection("backward")
    left = MoveDirection("left")
    right = MoveDirection("right")
    forwardLeft = MoveDirection("forwardLeft")
    forwardRight = MoveDirection("forwardRight")
    backwardLeft = MoveDirection("backwardLeft")
    backwardRight = MoveDirection("backwardRight")

    all = [stay, forward, backward, left, right, forwardLeft, forwardRight, backwardLeft, backwardRight]

    @staticmethod
    def getRandomMoveDirection():
        return MoveDirections.all[Random.getInt(0, len(MoveDirections.all) - 1)]


MoveDirections.stay.opposite = MoveDirections.stay
MoveDirections.forward.opposite = MoveDirections.backward
MoveDirections.backward.opposite = MoveDirections.forward
MoveDirections.left.opposite = MoveDirections.right
MoveDirections.right.opposite = MoveDirections.left
MoveDirections.forwardLeft.opposite = MoveDirections.backwardRight
MoveDirections.forwardRight.opposite = MoveDirections.backwardLeft
MoveDirections.backwardLeft.opposite = MoveDirections.forwardRight
MoveDirections.backwardRight.opposite = MoveDirections.forwardLeft

MoveDirections.stay.applyInputData = lambda _: None
MoveDirections.forward.applyInputData = lambda inputData: inputData.setGoForward()
MoveDirections.backward.applyInputData = lambda inputData: inputData.setGoBackward()
MoveDirections.left.applyInputData = lambda inputData: inputData.setStepLeft()
MoveDirections.right.applyInputData = lambda inputData: inputData.setStepRight()
MoveDirections.forwardLeft.applyInputData = lambda inputData: inputData.setGoForward().setStepLeft()
MoveDirections.forwardRight.applyInputData = lambda inputData: inputData.setGoForward().setStepRight()
MoveDirections.backwardLeft.applyInputData = lambda inputData: inputData.setGoBackward().setStepLeft()
MoveDirections.backwardRight.applyInputData = lambda inputData: inputData.setGoBackward().setStepRight()
