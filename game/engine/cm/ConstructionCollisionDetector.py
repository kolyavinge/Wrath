from game.engine.cm.PlaneCollisionDetector import PlaneCollisionDetector


class ConstructionCollisionDetector:

    def __init__(self, planeCollisionDetector):
        self.planeCollisionDetector = planeCollisionDetector

    def getConstructionCollisionResultOrNone(self, levelSegment, startPoint, endPoint):
        result = (
            self.getWallCollisionResultOrNone(levelSegment.walls, startPoint, endPoint)
            or self.getFloorCollisionResultOrNone(levelSegment.floors, startPoint, endPoint)
            or self.getCeilingCollisionResultOrNone(levelSegment.ceilings, startPoint, endPoint)
        )

        return result

    def getWallCollisionResultOrNone(self, walls, startPoint, endPoint):
        for wall in walls:
            collisionPoint = self.planeCollisionDetector.getCollisionPointOrNone(startPoint, endPoint, wall.downLeft, wall.frontNormal)
            if collisionPoint is not None and wall.containsPoint(collisionPoint):
                collisionPoint = wall.getNearestPointOnFront(collisionPoint)
                return (collisionPoint, wall.frontNormal)

        return None

    def getFloorCollisionResultOrNone(self, floors, startPoint, endPoint):
        if len(floors) > 0:
            floor = floors[0]
            collisionPoint = self.planeCollisionDetector.getCollisionPointOrNone(startPoint, endPoint, floor.downLeft, floor.frontNormal)
            if collisionPoint is not None and floor.containsPoint(collisionPoint):
                collisionPoint = floor.getNearestPointOnFront(collisionPoint)
                return (collisionPoint, floor.frontNormal)

        return None

    def getCeilingCollisionResultOrNone(self, ceilings, startPoint, endPoint):
        for ceiling in ceilings:
            collisionPoint = self.planeCollisionDetector.getCollisionPointOrNone(startPoint, endPoint, ceiling.downLeft, ceiling.frontNormal)
            if collisionPoint is not None and ceiling.containsPoint(collisionPoint):
                collisionPoint = ceiling.getNearestPointOnFront(collisionPoint)
                return (collisionPoint, ceiling.frontNormal)

        return None


def makeConstructionCollisionDetector(resolver):
    return ConstructionCollisionDetector(resolver.resolve(PlaneCollisionDetector))
