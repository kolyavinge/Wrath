from game.anx.Events import Events
from game.engine.bsp.BSPTreeTraversal import BSPTreeTraversal
from game.engine.BulletHoleFactory import BulletHoleFactory
from game.engine.cm.BulletCollisionDetector import BulletCollisionDetector
from game.engine.GameData import GameData
from game.lib.EventManager import EventManager


class BulletCollisionProcessor:

    def __init__(self, gameData, traversal, bulletCollisionDetector, bulletHoleFactory, eventManager):
        self.gameData = gameData
        self.traversal = traversal
        self.bulletCollisionDetector = bulletCollisionDetector
        self.bulletHoleFactory = bulletHoleFactory
        self.eventManager = eventManager

    def process(self):
        for bullet in self.gameData.bullets:
            collisionResult = self.bulletCollisionDetector.getConstructionCollisionResultOrNone(bullet)
            if collisionResult is None:
                bullet.commitNextPosition()
                bullet.currentLevelSegment = bullet.nextLevelSegment
            else:
                collisionPoint, frontNormal = collisionResult
                bspTree = self.gameData.level.visibilityTree
                visibilityLevelSegment = self.traversal.findLevelSegmentOrNone(bspTree, collisionPoint)
                bulletHole = self.bulletHoleFactory.make(collisionPoint, frontNormal, visibilityLevelSegment, bullet.holeInfo)
                self.gameData.bullets.remove(bullet)
                self.eventManager.raiseEvent(Events.bulletHoleAdded, bulletHole)


def makeBulletCollisionProcessor(resolver):
    return BulletCollisionProcessor(
        resolver.resolve(GameData),
        resolver.resolve(BSPTreeTraversal),
        resolver.resolve(BulletCollisionDetector),
        resolver.resolve(BulletHoleFactory),
        resolver.resolve(EventManager),
    )
