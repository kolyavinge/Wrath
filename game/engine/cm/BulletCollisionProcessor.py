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
            if collisionResult is not None:
                self.processCollision(bullet, collisionResult)
                return

            self.processNoCollision(bullet)

    def processCollision(self, bullet, collisionResult):
        collisionPoint, frontNormal = collisionResult
        bspTree = self.gameData.visibilityTree
        visibilityLevelSegment = self.traversal.findLevelSegmentOrNone(bspTree, collisionPoint)
        bullet.currentPosition = collisionPoint
        bullet.nextPosition = collisionPoint
        self.gameData.bullets.remove(bullet)
        if bullet.isVisible:
            bullet.currentVisibilityLevelSegment.bullets.remove(bullet)
        bulletHole = self.bulletHoleFactory.make(collisionPoint, frontNormal, visibilityLevelSegment, bullet.holeInfo)
        self.eventManager.raiseEvent(Events.bulletHoleAdded, bulletHole)

    def processNoCollision(self, bullet):
        if bullet.isVisible:
            oldVisibilityLevelSegment = bullet.currentVisibilityLevelSegment
            bullet.commitNextPosition()
            bullet.currentLevelSegment = bullet.nextLevelSegment
            bspTree = self.gameData.visibilityTree
            bullet.currentVisibilityLevelSegment = self.traversal.findLevelSegmentOrNone(bspTree, bullet.currentPosition)
            self.moveBulletToNewVisibilityLevelSegment(bullet, oldVisibilityLevelSegment, bullet.currentVisibilityLevelSegment)
        else:
            bullet.commitNextPosition()
            bullet.currentLevelSegment = bullet.nextLevelSegment

    def moveBulletToNewVisibilityLevelSegment(self, bullet, oldLevelSegment, newLevelSegment):
        if oldLevelSegment != newLevelSegment:
            oldLevelSegment.bullets.remove(bullet)
            newLevelSegment.bullets.append(bullet)


def makeBulletCollisionProcessor(resolver):
    return BulletCollisionProcessor(
        resolver.resolve(GameData),
        resolver.resolve(BSPTreeTraversal),
        resolver.resolve(BulletCollisionDetector),
        resolver.resolve(BulletHoleFactory),
        resolver.resolve(EventManager),
    )
