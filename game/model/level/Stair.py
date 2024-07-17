from game.calc.Vector3 import Vector3
from game.lib.Math import Math
from game.model.level.Floor import Floor


class Stair(Floor):
    def __init__(self):
        super().__init__()
        self.startBasePoint = Vector3()
        self.endBasePoint = Vector3()
        self.stepsCount = 0

    def commit(self):
        self.maxZ = self.endBasePoint.z
        self.stepDirection2d = self.endBasePoint.getCopy()
        self.stepDirection2d.sub(self.startBasePoint)
        self.stepDirection2d.z = 0
        self.stepsLength = self.stepDirection2d.getLength()
        self.stepDirection2d.normalize()
        self.stepHeight = (self.endBasePoint.z - self.startBasePoint.z) / self.stepsCount
        self.stepLength = self.stepsLength / self.stepsCount

    def getZ(self, x, y):
        position = Vector3(x, y, 0)
        position.sub(self.startBasePoint)
        position.z = 0
        projectedLength = position.dotProduct(self.stepDirection2d)
        z = (int(projectedLength / self.stepLength) + 1) * self.stepHeight
        z = Math.min(z, self.maxZ)

        return z
