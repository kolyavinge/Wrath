class Orientation:
    horizontal = 1
    vertical = 2
    diagonal = 3

    @staticmethod
    def getOpposite(x):
        if x == Orientation.horizontal:
            return Orientation.vertical

        if x == Orientation.vertical:
            return Orientation.horizontal

        if x == Orientation.diagonal:
            return Orientation.diagonal

        raise Exception()
