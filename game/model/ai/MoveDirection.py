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
