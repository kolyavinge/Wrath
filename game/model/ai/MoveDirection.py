class MoveDirection:

    idle = 0
    forward = 1
    backward = 2
    left = 3
    right = 4
    forwardLeft = 5
    forwardRight = 6
    backwardLeft = 7
    backwardRight = 8
    count = 9

    opposite = {
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
