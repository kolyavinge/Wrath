from game.engine.weapon.BulletHoleFactory import BulletHoleFactory


class BulletHoleLogic:

    def __init__(
        self,
        bulletHoleFactory: BulletHoleFactory,
    ):
        self.bulletHoleFactory = bulletHoleFactory

    def makeHole(self, gameState, collisionPoint, frontNormal, levelSegment, bulletHoleInfo):
        bulletHolePoint = self.toBulletHolePoint(collisionPoint)
        if bulletHolePoint not in gameState.bulletHolePoints:
            gameState.bulletHolePoints.add(bulletHolePoint)
            bulletHole = self.bulletHoleFactory.make(collisionPoint, frontNormal, levelSegment, bulletHoleInfo)
            gameState.updateStatistic.newBulletHoles.append(bulletHole)

    def toBulletHolePoint(self, collisionPoint):
        bulletHolePoint = collisionPoint.copy()
        bulletHolePoint.round(2)

        return bulletHolePoint
