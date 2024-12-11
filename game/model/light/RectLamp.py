from game.anx.CommonConstants import CommonConstants
from game.calc.Geometry import Geometry
from game.calc.Vector3 import Vector3
from game.lib.Math import Math
from game.model.light.Lamp import Lamp


class RectLamp(Lamp):

    def __init__(self):
        super().__init__()
        self.height = 0
        self.width = 0
        self.long = 0
        self.longNormal = Vector3()

    def getPoints(self):
        longHalf = self.longNormal.copy()
        longHalf.setLength(self.long / 2)
        widthHalf = Geometry.rotatePoint(self.longNormal, self.frontNormal, CommonConstants.axisOrigin, Math.piHalf)
        widthHalf.setLength(self.width / 2)

        upLeft = self.position.copy()
        upLeft.add(longHalf)
        upLeft.add(widthHalf)

        upRight = self.position.copy()
        upRight.add(longHalf)
        upRight.sub(widthHalf)

        downLeft = self.position.copy()
        downLeft.sub(longHalf)
        downLeft.add(widthHalf)

        downRight = self.position.copy()
        downRight.sub(longHalf)
        downRight.sub(widthHalf)

        resultBasePoints = [upRight, upLeft, downLeft, downRight]

        heightDirection = self.frontNormal.copy()
        heightDirection.setLength(self.height)
        resultFrontPoints = [upRight.copy(), upLeft.copy(), downLeft.copy(), downRight.copy()]
        for point in resultFrontPoints:
            point.add(heightDirection)

        resultNormals = [
            downLeft.getDirectionTo(upLeft),
            downRight.getDirectionTo(downLeft),
            upLeft.getDirectionTo(downLeft),
            downLeft.getDirectionTo(downRight),
        ]
        for point in resultNormals:
            point.normalize()

        resultBasePoints.append(resultBasePoints[0])
        resultFrontPoints.append(resultFrontPoints[0])

        return (resultBasePoints, resultFrontPoints, resultNormals)
