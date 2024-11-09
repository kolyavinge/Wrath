from game.lib.Numeric import Numeric


class PlaneCollisionDetector:

    def getCollisionPointOrNone(self, startPoint, endPoint, basePoint, frontNormal):
        if basePoint.getDirectionTo(endPoint).dotProduct(frontNormal) > 0:
            return None

        middlePoint = startPoint.getMiddleTo(endPoint)
        while startPoint.getLengthTo(endPoint) > 0.01:
            dotProduct = basePoint.getDirectionTo(middlePoint).dotProduct(frontNormal)
            if Numeric.floatEquals(dotProduct, 0, 0.1):
                break
            elif dotProduct > 0:
                startPoint = middlePoint
            else:
                endPoint = middlePoint
            middlePoint = startPoint.getMiddleTo(endPoint)

        return middlePoint


def makePlaneCollisionDetector(resolver):
    return PlaneCollisionDetector()
