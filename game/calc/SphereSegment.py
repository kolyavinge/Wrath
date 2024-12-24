from game.calc.Geometry import Geometry
from game.lib.Numeric import Numeric


class SphereSegment:

    def __init__(self, basePoint, centerPoint, rightNormal, horizontViewRadians, verticalViewRadians, horizontPoints, verticalPoints):
        if not Numeric.isOdd(horizontPoints):
            raise Exception("horizontPoints must be an odd number.")
        if not Numeric.isOdd(verticalPoints):
            raise Exception("verticalPoints must be an odd number.")

        self.points = []

        horizontRadiansStep = horizontViewRadians / (horizontPoints - 1)
        verticalRadiansStep = verticalViewRadians / (verticalPoints - 1)

        verticalRadians = verticalViewRadians / 2
        for _ in range(0, verticalPoints):
            rowCenter = Geometry.rotatePoint(centerPoint, rightNormal, basePoint, verticalRadians)

            upNormal = rightNormal.copy()
            upNormal.vectorProduct(rowCenter)
            upNormal.normalize()

            horizontRadians = horizontViewRadians / 2
            for _ in range(0, horizontPoints):
                self.points.append(Geometry.rotatePoint(rowCenter, upNormal, basePoint, horizontRadians))
                horizontRadians -= horizontRadiansStep

            verticalRadians -= verticalRadiansStep
