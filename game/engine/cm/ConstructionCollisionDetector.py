from game.anx.CommonConstants import CommonConstants
from game.engine.cm.PlaneCollisionDetector import PlaneCollisionDetector


class ConstructionCollisionDetector:

    def __init__(self, planeCollisionDetector: PlaneCollisionDetector):
        self.planeCollisionDetector = planeCollisionDetector

    def getCollisionResultOrNone(self, constructions, startPoint, endPoint, eps=0.1):
        result = None
        nearestLength = CommonConstants.maxLevelSize
        for construction in constructions:
            collisionPoint = self.planeCollisionDetector.getRectPlaneCollisionPointOrNone(startPoint, endPoint, construction.plane, eps)
            if collisionPoint is not None:
                collisionPoint = construction.plane.getNearestPointOnFront(collisionPoint)
                length = startPoint.getLengthTo(collisionPoint)
                if length < nearestLength:
                    result = (collisionPoint, construction)
                    nearestLength = length

        return result

    def getCollidedConstructionOrNone(self, constructions, startPoint, endPoint, eps=0.1):
        result = None
        nearestLength = CommonConstants.maxLevelSize
        for construction in constructions:
            collisionPoint = self.planeCollisionDetector.getRectPlaneCollisionPointOrNone(startPoint, endPoint, construction.plane, eps)
            if collisionPoint is not None:
                length = startPoint.getLengthTo(collisionPoint)
                if length < nearestLength:
                    result = construction
                    nearestLength = length

        return result

    def isCollidedConstruction(self, construction, startPoint, endPoint, eps=0.1):
        return self.planeCollisionDetector.getRectPlaneCollisionPointOrNone(startPoint, endPoint, construction.plane, eps) is not None
