from game.anx.CommonConstants import CommonConstants
from game.engine.cm.PlaneCollisionDetector import PlaneCollisionDetector


class ConstructionCollisionDetector:

    def __init__(self, planeCollisionDetector: PlaneCollisionDetector):
        self.planeCollisionDetector = planeCollisionDetector

    def getCollisionResultOrNone(self, allConstructions, startPoint, endPoint):
        result = None
        nearestLength = CommonConstants.maxLevelSize
        for construction in allConstructions:
            collisionPoint = self.planeCollisionDetector.getRectPlaneCollisionPointOrNone(startPoint, endPoint, construction.plane, 0.1)
            if collisionPoint is not None:
                collisionPoint = construction.plane.getNearestPointOnFront(collisionPoint)
                length = startPoint.getLengthTo(collisionPoint)
                if length < nearestLength:
                    result = (collisionPoint, construction.frontNormal)
                    nearestLength = length

        return result
