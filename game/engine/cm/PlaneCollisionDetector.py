from game.lib.calc.Vector3 import Vector3


class PlaneCollisionDetector:

    def getRectPlaneCollisionPointOrNone(self, startPoint, endPoint, rectPlane, eps):
        collisionPoint = self.getPlaneCollisionPointOrNone(startPoint, endPoint, rectPlane.downLeft, rectPlane.normal, eps)
        if collisionPoint is not None and rectPlane.containsPoint(collisionPoint, eps):
            return collisionPoint
        else:
            return None

    def getPlaneCollisionPointOrNone(self, startPoint, endPoint, basePoint, frontNormal, eps):
        startPointDotProduct = Vector3.calcDirectionAndGetDotProduct(basePoint, startPoint, frontNormal)
        endPointDotProduct = Vector3.calcDirectionAndGetDotProduct(basePoint, endPoint, frontNormal)

        # чтобы пересечение было, скалярные произведения должны иметь разные знаки
        if startPointDotProduct * endPointDotProduct > 0:
            return None

        # для работы алгоритма startPoint должна находится перед лицевой стороной плоскости (dotProduct > 0)
        if startPointDotProduct < 0:
            # такая ситуация возможна, если мы находим пересечение с обьектом, представленным в виде пересекающихся плоскостей
            # поворачивам плоскость на 180 градусов
            # (лучше повернуть плоскость, а не менять местами startPoint и endPoint)
            frontNormal = frontNormal.copy()
            frontNormal.mul(-1)

        length = startPoint.getLengthTo(endPoint)
        middlePoint = startPoint.getMiddleTo(endPoint)
        while length > eps:
            dotProduct = Vector3.calcDirectionAndGetDotProduct(basePoint, middlePoint, frontNormal)
            if dotProduct > 0:
                startPoint = middlePoint
            else:
                endPoint = middlePoint
            length /= 2.0
            middlePoint = startPoint.getMiddleTo(endPoint)

        # в качестве окончательной точки пересечения берем startPoint
        # результирующая точка должна лежать перед лицевой стороной плоскости
        return startPoint
