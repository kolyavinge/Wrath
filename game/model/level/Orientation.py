class Orientation:
    horizontal = 1
    vertical = 2

    @staticmethod
    def getOpposite(x):
        if x == Orientation.horizontal:
            return Orientation.vertical
        else:
            return Orientation.horizontal
