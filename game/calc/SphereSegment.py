from game.calc.Geometry import Geometry
from game.lib.Numeric import Numeric


class SphereSegment:

    def __init__(self, basePoint, centerPoint, rightNormal, horizontalViewRadians, verticalViewRadians, horizontalPoints, verticalPoints):
        if not Numeric.isOdd(horizontalPoints):
            raise Exception("horizontalPoints must be an odd number.")
        if not Numeric.isOdd(verticalPoints):
            raise Exception("verticalPoints must be an odd number.")

        self.points = []

        horizontalRadiansStep = horizontalViewRadians / (horizontalPoints - 1)
        verticalRadiansStep = verticalViewRadians / (verticalPoints - 1)

        verticalRadians = verticalViewRadians / 2
        for _ in range(0, verticalPoints):
            rowCenter = Geometry.rotatePoint(centerPoint, rightNormal, basePoint, verticalRadians)

            upNormal = rightNormal.copy()
            upNormal.vectorProduct(rowCenter)
            upNormal.normalize()

            horizontalRadians = horizontalViewRadians / 2
            for _ in range(0, horizontalPoints):
                self.points.append(Geometry.rotatePoint(rowCenter, upNormal, basePoint, horizontalRadians))
                horizontalRadians -= horizontalRadiansStep

            verticalRadians -= verticalRadiansStep
