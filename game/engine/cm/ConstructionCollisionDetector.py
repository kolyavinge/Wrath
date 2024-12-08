from game.engine.cm.PlaneCollisionDetector import PlaneCollisionDetector


class ConstructionCollisionDetector:

    def __init__(self, planeCollisionDetector):
        self.planeCollisionDetector = planeCollisionDetector

    def getCollisionResultOrNone(self, levelSegment, startPoint, endPoint):
        result = (
            self.getConstructionCollisionResultOrNone(levelSegment.constructions, startPoint, endPoint)
            or self.getConstructionCollisionResultOrNone(levelSegment.walls, startPoint, endPoint)
            or self.getConstructionCollisionResultOrNone(levelSegment.floors, startPoint, endPoint)
            or self.getConstructionCollisionResultOrNone(levelSegment.ceilings, startPoint, endPoint)
        )

        return result

    def getConstructionCollisionResultOrNone(self, constructions, startPoint, endPoint):
        for construction in constructions:
            collisionPoint = self.planeCollisionDetector.getCollisionPointOrNone(
                startPoint, endPoint, construction.downLeft, construction.frontNormal
            )
            if collisionPoint is not None and construction.containsPoint(collisionPoint):
                collisionPoint = construction.getNearestPointOnFront(collisionPoint)
                return (collisionPoint, construction.frontNormal)

        return None


def makeConstructionCollisionDetector(resolver):
    return ConstructionCollisionDetector(resolver.resolve(PlaneCollisionDetector))
