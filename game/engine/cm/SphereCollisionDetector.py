from game.engine.cm.PlaneCollisionDetector import PlaneCollisionDetector


class SphereCollisionDetector:

    def __init__(self, planeCollisionDetector: PlaneCollisionDetector):
        self.planeCollisionDetector = planeCollisionDetector

    def getCollisionPointOrNone(self, startPoint, endPoint, centerPoint, radius, eps):
        frontNormal = endPoint.getDirectionTo(startPoint)
        if frontNormal.isZero():
            return None

        frontNormal.normalize()
        collisionPoint = self.planeCollisionDetector.getPlaneCollisionPointOrNone(startPoint, endPoint, centerPoint, frontNormal, eps)
        if collisionPoint is not None and collisionPoint.getLengthTo(centerPoint) <= radius:
            return collisionPoint
        else:
            return None
