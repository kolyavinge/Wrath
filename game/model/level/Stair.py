from game.calc.Geometry import Geometry
from game.calc.Vector3 import Vector3


class Stair:
    def __init__(self):
        self.downLeft = Vector3()
        self.downRight = Vector3()
        self.upLeft = Vector3()
        self.upRight = Vector3()
        self.leftFrontNormal = Vector3()
        self.rightFrontNormal = Vector3()
        self.upFrontNormal = Vector3()
        self.downFrontNormal = Vector3()
        self.startBasePoint = Vector3()
        self.endBasePoint = Vector3()
        self.stepsCount = 0

    def commit(self):
        self.stepDirection2d = self.endBasePoint.getCopy()
        self.stepDirection2d.sub(self.startBasePoint)
        self.stepDirection2d.z = 0
        self.stepDirection2d.normalize()
        self.stepHeight = (self.endBasePoint.z - self.startBasePoint.z) / self.stepsCount
        self.stepLength = 0

    def getZ(self, x, y):
        position = Vector3(x, y, 0)
        position.sub(self.startBasePoint)
        position.z = 0
        projectedLength = position.dotProduct(self.stepDirection2d)
        z = int(projectedLength / self.stepLength) * self.stepHeight

        return z
