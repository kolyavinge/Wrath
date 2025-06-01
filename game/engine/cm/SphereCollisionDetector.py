from game.engine.cm.PlaneCollisionDetector import PlaneCollisionDetector


class SphereCollisionDetector:

    def __init__(self, planeCollisionDetector: PlaneCollisionDetector):
        self.planeCollisionDetector = planeCollisionDetector

    def getSphereCollisionPointOrNone(self, startPoint, endPoint, centerPoint, radius, eps):
        frontNormal = endPoint.getDirectionTo(startPoint).getNormalized()
        collisionPoint = self.planeCollisionDetector.getPlaneCollisionPointOrNone(startPoint, endPoint, centerPoint, frontNormal, eps)
        if collisionPoint is not None and collisionPoint.getLengthTo(centerPoint) <= radius:
            return collisionPoint
        else:
            return None
