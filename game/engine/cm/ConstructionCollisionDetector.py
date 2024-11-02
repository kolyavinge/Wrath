from game.calc.Vector3 import Vector3
from game.lib.Numeric import Numeric


class ConstructionCollisionDetector:

    def getConstructionCollisionResultOrNone(self, levelSegment, startPoint, endPoint):
        result = (
            self.getWallCollisionResultOrNone(levelSegment.walls, startPoint, endPoint)
            or self.getFloorCollisionResultOrNone(levelSegment.floors, startPoint, endPoint)
            or self.getCeilingCollisionResultOrNone(levelSegment.ceilings, startPoint, endPoint)
        )

        return result

    def getWallCollisionResultOrNone(self, walls, startPoint, endPoint):
        for wall in walls:
            collisionPoint = self.getPossibleCollisionPointOrNone(startPoint, endPoint, wall.downLeft, wall.frontNormal)
            if collisionPoint is not None and wall.containsPoint(collisionPoint):
                collisionPoint = self.getCollisionPointOnFrontSide(collisionPoint, wall)
                # print("wall", wall)
                return (collisionPoint, wall.frontNormal)

        return None

    def getFloorCollisionResultOrNone(self, floors, startPoint, endPoint):
        if len(floors) > 0:
            floor = floors[0]
            collisionPoint = self.getPossibleCollisionPointOrNone(startPoint, endPoint, floor.downLeft, floor.frontNormal)
            if collisionPoint is not None and floor.containsPoint(collisionPoint):
                collisionPoint = self.getCollisionPointOnFrontSide(collisionPoint, floor)
                # print("floor", floor)
                return (collisionPoint, floor.frontNormal)

        return None

    def getCeilingCollisionResultOrNone(self, ceilings, startPoint, endPoint):
        for ceiling in ceilings:
            collisionPoint = self.getPossibleCollisionPointOrNone(startPoint, endPoint, ceiling.downLeft, ceiling.frontNormal)
            if collisionPoint is not None and ceiling.containsPoint(collisionPoint):
                collisionPoint = self.getCollisionPointOnFrontSide(collisionPoint, ceiling)
                # print("ceiling", ceiling)
                return (collisionPoint, ceiling.frontNormal)

        return None

    def getPossibleCollisionPointOrNone(self, startPoint, endPoint, basePoint, frontNormal):
        if basePoint.getDirectionTo(endPoint).dotProduct(frontNormal) > 0:
            return None

        middlePoint = Vector3.getMiddlePoint(startPoint, endPoint)
        while Vector3.getLengthBetween(startPoint, endPoint) > 0.01:
            dotProduct = basePoint.getDirectionTo(middlePoint).dotProduct(frontNormal)
            if Numeric.floatEquals(dotProduct, 0, 0.1):
                break
            elif dotProduct > 0:
                startPoint = middlePoint
            else:
                endPoint = middlePoint
            middlePoint = Vector3.getMiddlePoint(startPoint, endPoint)

        return middlePoint

    def getCollisionPointOnFrontSide(self, collisionPoint, construction):
        projected = construction.getProjectedPoint(collisionPoint)
        frontNormal = construction.frontNormal.copy()
        frontNormal.setLength(0.001)
        projected.add(frontNormal)

        return projected


def makeConstructionCollisionDetector(resolver):
    return ConstructionCollisionDetector()
