class Orientation:
    horizontal = 1
    vertical = 2
    diagonalDownLeftUpRight = 3
    diagonalUpLeftDownRight = 4

    @staticmethod
    def getOpposite(x):
        if x == Orientation.horizontal:
            return Orientation.vertical

        if x == Orientation.vertical:
            return Orientation.horizontal

        if x == Orientation.diagonalDownLeftUpRight:
            return Orientation.diagonalUpLeftDownRight

        if x == Orientation.diagonalUpLeftDownRight:
            return Orientation.diagonalDownLeftUpRight

        raise Exception()
