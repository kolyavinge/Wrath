from game.anx.CommonConstants import CommonConstants
from game.calc.Vector3 import Vector3
from game.lib.Numeric import Numeric


class BulletCollisionDetector:

    def getConstructionCollisionResultOrNone(self, bullet):
        levelSegment = bullet.levelSegment
        result = (
            self.getWallCollisionResultOrNone(levelSegment.walls, bullet)
            or self.getFloorCollisionResultOrNone(levelSegment.floors, bullet)
            or self.getCeilingCollisionResultOrNone(levelSegment.ceilings, bullet)
        )

        return result

    def getWallCollisionResultOrNone(self, walls, bullet):
        resultCollisionPoint = None
        resultWallFrontNormal = None
        nearestWallLength = CommonConstants.maxLevelSize
        for wall in walls:
            collisionPoint = self.getPossibleCollisionPointOrNone(bullet.currentPosition, bullet.nextPosition, wall.downLeft, wall.frontNormal)
            if collisionPoint is not None and wall.containsPoint(collisionPoint):
                # print("wall", wall)
                if Vector3.getLengthBetween(bullet.currentPosition, collisionPoint) < nearestWallLength:
                    collisionPoint = self.getCollisionPointOnFrontSide(collisionPoint, wall)
                    nearestWallLength = Vector3.getLengthBetween(bullet.currentPosition, collisionPoint)
                    resultCollisionPoint = collisionPoint
                    resultWallFrontNormal = wall.frontNormal

        if resultCollisionPoint is not None:
            return (resultCollisionPoint, resultWallFrontNormal)
        else:
            return None

    def getFloorCollisionResultOrNone(self, floors, bullet):
        if len(floors) > 0:
            floor = floors[0]
            collisionPoint = self.getPossibleCollisionPointOrNone(bullet.currentPosition, bullet.nextPosition, floor.downLeft, floor.frontNormal)
            if collisionPoint is not None and floor.containsPoint(collisionPoint):
                collisionPoint = self.getCollisionPointOnFrontSide(collisionPoint, floor)
                # print("floor", floor)
                return (collisionPoint, floor.frontNormal)

        return None

    def getCeilingCollisionResultOrNone(self, ceilings, bullet):
        for ceiling in ceilings:
            collisionPoint = self.getPossibleCollisionPointOrNone(bullet.currentPosition, bullet.nextPosition, ceiling.downLeft, ceiling.frontNormal)
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


def makeBulletCollisionDetector(resolver):
    return BulletCollisionDetector()
