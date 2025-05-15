from game.calc.Vector3 import Vector3
from game.lib.Numeric import Numeric


class MoveDirection:

    idle = "idle"
    forward = "forward"
    backward = "backward"
    left = "left"
    right = "right"
    forwardLeft = "forwardLeft"
    forwardRight = "forwardRight"
    backwardLeft = "backwardLeft"
    backwardRight = "backwardRight"

    all = [idle, forward, backward, left, right, forwardLeft, forwardRight, backwardLeft, backwardRight]

    opposite = {
        idle: idle,
        forward: backward,
        backward: forward,
        left: right,
        right: left,
        forwardLeft: backwardRight,
        forwardRight: backwardLeft,
        backwardLeft: forwardRight,
        backwardRight: forwardLeft,
    }

    @staticmethod
    def getOpposite(direction):
        if direction in MoveDirection.opposite:
            return MoveDirection.opposite[direction]
        else:
            raise Exception(f"No opposite direction for {direction}.")

    @staticmethod
    def fromVector(vector):
        v = Vector3(vector.x, vector.y, 0.0).getNormalized()
        delta = 0.2

        if Numeric.floatEquals(v.x, 0.0, delta) and Numeric.floatEquals(v.y, 1.0, delta):
            return MoveDirection.forward

        if Numeric.floatEquals(v.x, 0.0, delta) and Numeric.floatEquals(v.y, -1.0, delta):
            return MoveDirection.backward

        if Numeric.floatEquals(v.x, 1.0, delta) and Numeric.floatEquals(v.y, 0.0, delta):
            return MoveDirection.right

        if Numeric.floatEquals(v.x, -1.0, delta) and Numeric.floatEquals(v.y, 0.0, delta):
            return MoveDirection.left

        if v.x > 0.0 and v.y > 0.0:
            return MoveDirection.forwardRight

        if v.x < 0.0 and v.y > 0.0:
            return MoveDirection.forwardLeft

        if v.x > 0.0 and v.y < 0.0:
            return MoveDirection.backwardRight

        return MoveDirection.backwardLeft
