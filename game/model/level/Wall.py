from game.calc.Vector3 import Vector3


class WallOrientation:
    horizontal = 1
    vertical = 2

    @staticmethod
    def getOpposite(x):
        if x == WallOrientation.horizontal:
            return WallOrientation.vertical
        else:
            return WallOrientation.horizontal


class Wall:

    def __init__(self):
        self.orientation = WallOrientation.horizontal
        self.startPosition = Vector3()
        self.endPosition = Vector3()
        self.frontNormal = Vector3()

    def getMinX(self):
        return min(self.startPosition.x, self.endPosition.x)

    def getMaxX(self):
        return max(self.startPosition.x, self.endPosition.x)

    def getMinY(self):
        return min(self.startPosition.y, self.endPosition.y)

    def getMaxY(self):
        return max(self.startPosition.y, self.endPosition.y)

    def validate(self):
        if self.orientation != WallOrientation.horizontal and self.orientation != WallOrientation.vertical:
            raise Exception()

        if self.startPosition == self.endPosition:
            raise Exception()

        if self.frontNormal.isZero():
            raise Exception()

        if self.frontNormal.getLength() != 1:
            raise Exception()

    def toString(self):
        return f"({self.startPosition.toString()} - {self.endPosition.toString()})"
