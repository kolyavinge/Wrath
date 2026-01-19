from game.engine.weapon.BulletHoleFactory import BulletHoleFactory
from game.lib.EventManager import EventManager, Events


class BulletHoleLogic:

    def __init__(
        self,
        bulletHoleFactory: BulletHoleFactory,
        eventManager: EventManager,
    ):
        self.bulletHoleFactory = bulletHoleFactory
        self.eventManager = eventManager

    def makeHole(self, gameState, collisionPoint, frontNormal, levelSegment, bulletHoleInfo):
        bulletHolePoint = self.toBulletHolePoint(collisionPoint)
        if bulletHolePoint not in gameState.bulletHolePoints:
            gameState.bulletHolePoints.add(bulletHolePoint)
            bulletHole = self.bulletHoleFactory.make(collisionPoint, frontNormal, levelSegment, bulletHoleInfo)
            self.eventManager.raiseEvent(Events.bulletHoleAdded, bulletHole)

    def toBulletHolePoint(self, collisionPoint):
        bulletHolePoint = collisionPoint.copy()
        bulletHolePoint.round(2)

        return bulletHolePoint
