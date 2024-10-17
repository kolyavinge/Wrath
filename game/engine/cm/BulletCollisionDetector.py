from game.calc.Vector3 import Vector3
from game.lib.Numeric import Numeric


class BulletCollisionDetector:

    def getConstructionCollisionPointOrNone(self, bullet):
        levelSegment = bullet.currentLevelSegment

        for wall in levelSegment.walls:
            collisionPoint = self.getPossibleCollisionPointOrNone(bullet.currentPosition, bullet.nextPosition, wall.downLeft, wall.frontNormal)
            if collisionPoint is not None and wall.inRect(collisionPoint):
                print("wall", wall)
                return collisionPoint

        if len(levelSegment.floors) > 0:
            floor = levelSegment.floors[0]
            collisionPoint = self.getPossibleCollisionPointOrNone(bullet.currentPosition, bullet.nextPosition, floor.downLeft, floor.frontNormal)
            if collisionPoint is not None and floor.inRect(collisionPoint):
                print("floor", floor)
                return collisionPoint

        for ceiling in levelSegment.ceilings:
            collisionPoint = self.getPossibleCollisionPointOrNone(bullet.currentPosition, bullet.nextPosition, ceiling.downLeft, ceiling.frontNormal)
            if collisionPoint is not None and ceiling.inRect(collisionPoint):
                print("ceiling", ceiling)
                return collisionPoint

        return None

    def getPossibleCollisionPointOrNone(self, startPoint, endPoint, basePoint, frontNormal):
        if basePoint.getDirectionTo(endPoint).dotProduct(frontNormal) > 0:
            return None

        middlePoint = Vector3.getMiddlePoint(startPoint, endPoint)
        while Vector3.getLengthBetween(startPoint, endPoint) > 0.1:
            dotProduct = basePoint.getDirectionTo(middlePoint).dotProduct(frontNormal)
            if Numeric.floatEquals(dotProduct, 0, 0.1):
                break
            elif dotProduct > 0:
                startPoint = middlePoint
            else:
                endPoint = middlePoint
            middlePoint = Vector3.getMiddlePoint(startPoint, endPoint)

        return middlePoint


def makeBulletCollisionDetector(resolver):
    return BulletCollisionDetector()
