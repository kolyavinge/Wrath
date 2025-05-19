class MoveDirection:
    pass


class MoveDirections:

    stay = MoveDirection()
    forward = MoveDirection()
    backward = MoveDirection()
    left = MoveDirection()
    right = MoveDirection()
    forwardLeft = MoveDirection()
    forwardRight = MoveDirection()
    backwardLeft = MoveDirection()
    backwardRight = MoveDirection()

    all = [stay, forward, backward, left, right, forwardLeft, forwardRight, backwardLeft, backwardRight]


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
