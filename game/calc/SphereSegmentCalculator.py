from game.calc.Geometry import Geometry
from game.calc.Point2 import Point2
from game.lib.Math import Math
from game.lib.Numeric import Numeric


class SphereSegmentCalculator:

    def getVertices(self, basePoint, centerPoint, rightNormal, horizontalViewRadians, verticalViewRadians, horizontalPoints, verticalPoints):
        self.verifyParams(horizontalPoints, verticalPoints)
        horizontalRadiansStep = horizontalViewRadians / (horizontalPoints - 1)
        verticalRadiansStep = verticalViewRadians / (verticalPoints - 1)
        verticalRadians = verticalViewRadians / 2
        result = []
        for _ in range(0, verticalPoints):
            rowCenter = Geometry.rotatePoint(centerPoint, rightNormal, basePoint, verticalRadians)

            upNormal = rightNormal.copy()
            upNormal.vectorProduct(rowCenter)
            upNormal.normalize()

            horizontalRadians = horizontalViewRadians / 2
            for _ in range(0, horizontalPoints):
                result.append(Geometry.rotatePoint(rowCenter, upNormal, basePoint, horizontalRadians))
                horizontalRadians -= horizontalRadiansStep

            verticalRadians -= verticalRadiansStep

        return result

    def getTexCoords(self, yawRadians, pitchRadians, horizontalViewRadians, verticalViewRadians, horizontalPoints, verticalPoints):
        self.verifyParams(horizontalPoints, verticalPoints)
        centerX = 0.5 - yawRadians / Math.piDouble
        centerY = 0.5 - pitchRadians / Math.piDouble
        lengthX = horizontalViewRadians / Math.piDouble
        lengthY = verticalViewRadians / Math.piDouble
        stepX = lengthX / (horizontalPoints - 1)
        stepY = lengthY / (verticalPoints - 1)
        upLeftX = centerX - (lengthX / 2)
        upLeftY = centerY - (lengthY / 2)
        coordsX = [upLeftX + i * stepX for i in range(0, horizontalPoints)]
        coordsY = [upLeftY + i * stepY for i in range(0, verticalPoints)]
        result = []
        for y in coordsY:
            for x in coordsX:
                result.append(Point2(x, y))

        return result

    def verifyParams(self, horizontalPoints, verticalPoints):
        if not Numeric.isOdd(horizontalPoints):
            raise Exception("horizontalPoints must be an odd number.")
        if not Numeric.isOdd(verticalPoints):
            raise Exception("verticalPoints must be an odd number.")
