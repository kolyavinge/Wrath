from game.calc.Vector3 import Vector3
from game.lib.Numeric import Numeric


class BulletCollisionDetector:

    def getConstructionCollisionResultOrNone(self, bullet):
        levelSegment = bullet.levelSegment

        for wall in levelSegment.walls:
            collisionPoint = self.getPossibleCollisionPointOrNone(bullet.currentPosition, bullet.nextPosition, wall.downLeft, wall.frontNormal)
            if collisionPoint is not None and wall.containsPoint(collisionPoint):
                collisionPoint = self.shiftCollisionPointOnFrontSide(collisionPoint, wall.frontNormal)
                # print("wall", wall)
                return (collisionPoint, wall.frontNormal)

        if len(levelSegment.floors) > 0:
            floor = levelSegment.floors[0]
            collisionPoint = self.getPossibleCollisionPointOrNone(bullet.currentPosition, bullet.nextPosition, floor.downLeft, floor.frontNormal)
            if collisionPoint is not None and floor.containsPoint(collisionPoint):
                collisionPoint = self.shiftCollisionPointOnFrontSide(collisionPoint, floor.frontNormal)
                # print("floor", floor)
                return (collisionPoint, floor.frontNormal)

        for ceiling in levelSegment.ceilings:
            collisionPoint = self.getPossibleCollisionPointOrNone(bullet.currentPosition, bullet.nextPosition, ceiling.downLeft, ceiling.frontNormal)
            if collisionPoint is not None and ceiling.containsPoint(collisionPoint):
                collisionPoint = self.shiftCollisionPointOnFrontSide(collisionPoint, ceiling.frontNormal)
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

    def shiftCollisionPointOnFrontSide(self, collisionPoint, frontNormal):
        frontNormal = frontNormal.copy()
        frontNormal.setLength(0.5)
        collisionPoint.add(frontNormal)

        return collisionPoint


def makeBulletCollisionDetector(resolver):
    return BulletCollisionDetector()
