from game.anx.CommonConstants import CommonConstants
from game.engine.cm.PlaneCollisionDetector import PlaneCollisionDetector


class ConstructionCollisionDetector:

    def __init__(self, planeCollisionDetector):
        self.planeCollisionDetector = planeCollisionDetector

    def getCollisionResultOrNone(self, levelSegment, startPoint, endPoint):
        resultCollisionPoint = None
        nearestLength = CommonConstants.maxLevelSize
        for construction in levelSegment.allConstructions:
            collisionPoint = self.planeCollisionDetector.getCollisionPointOrNone(
                startPoint, endPoint, construction.downLeft, construction.frontNormal
            )
            if collisionPoint is not None and construction.containsPoint(collisionPoint):
                collisionPoint = construction.getNearestPointOnFront(collisionPoint)
                length = startPoint.getLengthTo(collisionPoint)
                if length < nearestLength:
                    resultCollisionPoint = (collisionPoint, construction.frontNormal)
                    nearestLength = length

        return resultCollisionPoint


def makeConstructionCollisionDetector(resolver):
    return ConstructionCollisionDetector(resolver.resolve(PlaneCollisionDetector))
