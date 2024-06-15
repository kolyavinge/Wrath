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
        self.check(self.orientation == WallOrientation.horizontal or self.orientation == WallOrientation.vertical)
        self.check(self.startPosition != self.endPosition)
        self.check(self.frontNormal.getLength() == 1)
        if self.orientation == WallOrientation.horizontal:
            self.check(self.startPosition.y == self.endPosition.y)
            self.check(self.startPosition.x < self.endPosition.x)
            self.check(self.frontNormal == Vector3(0, 1, 0) or self.frontNormal == Vector3(0, -1, 0))
        elif self.orientation == WallOrientation.vertical:
            self.check(self.startPosition.x == self.endPosition.x)
            self.check(self.startPosition.y < self.endPosition.y)
            self.check(self.frontNormal == Vector3(1, 0, 0) or self.frontNormal == Vector3(-1, 0, 0))

    def check(self, value):
        if value == False:
            raise Exception()

    def toString(self):
        return f"({self.startPosition.toString()} - {self.endPosition.toString()})"
