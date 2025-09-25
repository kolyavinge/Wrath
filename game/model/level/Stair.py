from game.anx.CommonConstants import CommonConstants
from game.calc.Geometry import Geometry
from game.calc.Vector3 import Vector3
from game.lib.Math import Math
from game.model.FaceDirection import FaceDirection
from game.model.level.Floor import Floor


class Stair(Floor):

    def __init__(self):
        super().__init__()
        self.startBasePoint = Vector3()
        self.endBasePoint = Vector3()
        self.stepsCount = 0
        self.stepWidth = 0
        self.includeBorderPoints = True
        self.slowdownCoeff = 0.5

    def commit(self):
        self.maxZ = self.endBasePoint.z
        self.stepDirection2d = self.startBasePoint.getDirectionTo(self.endBasePoint)
        self.stepDirection2d.z = 0
        self.stepsLength = self.stepDirection2d.getLength()
        self.stepDirection2d.normalize()
        self.stepHeight = (self.endBasePoint.z - self.startBasePoint.z) / self.stepsCount
        self.stepLength = self.stepsLength / self.stepsCount
        # frontNormal - нормаль передней грани ступеньки
        # topNormal - нормаль верхней грани
        self.frontNormal = CommonConstants.zAxis
        self.topNormal = Geometry.rotatePoint(self.frontNormal, CommonConstants.zAxis, CommonConstants.axisOrigin, Math.piHalf)
        self.topNormal.normalize()
        super().commit()
        self.isHorizontal = False

    def getFaceDirection(self):
        return FaceDirection.counterClockwise

    def getBorderPoints(self):
        return [
            self.downLeft,
            self.downRight,
            self.upLeft,
            self.upRight,
            Vector3(self.downLeft.x, self.downLeft.y, self.maxZ),
            Vector3(self.downRight.x, self.downRight.y, self.maxZ),
            Vector3(self.upLeft.x, self.upLeft.y, self.maxZ),
            Vector3(self.upRight.x, self.upRight.y, self.maxZ),
        ]

    def getZ(self, x, y):
        position = Vector3(x, y, 0)
        position.sub(self.startBasePoint)
        position.z = 0
        projectedLength = position.dotProduct(self.stepDirection2d)
        z = (int(projectedLength / self.stepLength) + 1) * self.stepHeight + self.startBasePoint.z
        z = Math.min(z, self.maxZ)

        return z

    def getFrontAndTopFacePoints(self, stepNumber):
        rightDirection = self.getLeftToRightDirection()

        downLeft = self.getDownLeftStepPoint(stepNumber)
        downRight = downLeft.copy()
        downRight.add(rightDirection)
        upLeft = downLeft.copy()
        upLeft.z += self.stepHeight
        upRight = downRight.copy()
        upRight.z += self.stepHeight

        frontFace = (downLeft, downRight, upLeft, upRight)

        stepLengthDirection = self.stepDirection2d.copy()
        stepLengthDirection.setLength(self.stepLength)

        downLeft = upLeft.copy()
        downRight = upRight.copy()
        upLeft = downLeft.copy()
        upLeft.add(stepLengthDirection)
        upRight = downRight.copy()
        upRight.add(stepLengthDirection)

        topFace = (downLeft, downRight, upLeft, upRight)

        return (frontFace, topFace)

    def getLeftToRightDirection(self):
        rightDirection = self.startBasePoint.getDirectionTo(self.endBasePoint)
        rightDirection.z = 0
        rightDirection = Geometry.rotatePoint(rightDirection, CommonConstants.zAxis, CommonConstants.axisOrigin, -Math.piHalf)
        rightDirection.setLength(self.stepWidth)

        return rightDirection

    def getDownLeftStepPoint(self, stepNumber):
        stepDirection = self.startBasePoint.getDirectionTo(self.endBasePoint)
        stepDirection.div(self.stepsCount)
        stepDirection.mul(stepNumber)
        downLeft = self.startBasePoint.copy()
        downLeft.add(stepDirection)

        return downLeft
