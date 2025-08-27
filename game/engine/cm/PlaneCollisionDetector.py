from game.lib.Numeric import Numeric


class PlaneCollisionDetector:

    def getRectPlaneCollisionPointOrNone(self, startPoint, endPoint, rectPlane, eps):
        collisionPoint = self.getPlaneCollisionPointOrNone(startPoint, endPoint, rectPlane.downLeft, rectPlane.normal, eps)
        if collisionPoint is not None and rectPlane.containsPoint(collisionPoint, eps):
            return collisionPoint
        else:
            return None

    def getPlaneCollisionPointOrNone(self, startPoint, endPoint, basePoint, frontNormal, eps):
        startPointDotProduct = basePoint.getDirectionTo(startPoint).dotProduct(frontNormal)
        endPointDotProduct = basePoint.getDirectionTo(endPoint).dotProduct(frontNormal)

        # чтобы пересечение было, скалярные произведения должны иметь разные знаки
        if startPointDotProduct * endPointDotProduct > 0:
            return None

        # для работы алгоритма startPoint должна находится перед лицевой стороной плоскости (dotProduct > 0)
        if startPointDotProduct < 0:
            # поворачивам плоскость на 180 градусов
            frontNormal = frontNormal.copy()
            frontNormal.mul(-1)

        middlePoint = startPoint.getMiddleTo(endPoint)
        while startPoint.getLengthTo(endPoint) > eps:
            dotProduct = basePoint.getDirectionTo(middlePoint).dotProduct(frontNormal)
            if Numeric.floatEquals(dotProduct, 0):
                break
            elif dotProduct > 0:
                startPoint = middlePoint
            else:
                endPoint = middlePoint
            middlePoint = startPoint.getMiddleTo(endPoint)

        return middlePoint
