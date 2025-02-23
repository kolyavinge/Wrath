from game.lib.Numeric import Numeric


class PlaneCollisionDetector:

    def getRectPlaneCollisionPointOrNone(self, startPoint, endPoint, rectPlane, eps):
        collisionPoint = self.getPlaneCollisionPointOrNone(startPoint, endPoint, rectPlane.downLeft, rectPlane.normal)
        if collisionPoint is not None and rectPlane.containsPoint(collisionPoint, eps):
            return collisionPoint
        else:
            return None

    def getPlaneCollisionPointOrNone(self, startPoint, endPoint, basePoint, frontNormal):
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
