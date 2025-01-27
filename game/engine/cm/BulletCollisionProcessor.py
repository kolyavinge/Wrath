from game.anx.Events import Events
from game.anx.PersonConstants import PersonConstants
from game.engine.bsp.BSPTreeTraversal import BSPTreeTraversal
from game.engine.BulletHoleFactory import BulletHoleFactory
from game.engine.cm.BulletCollisionDetector import *
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
            collisionResult = self.bulletCollisionDetector.getCollisionResultOrNone(bullet)
            if collisionResult is not None:
                self.processCollision(bullet, collisionResult)

    def processCollision(self, bullet, collisionResult):
        self.gameData.bullets.remove(bullet)
        if bullet.isVisible:
            bullet.currentVisibilityLevelSegment.bullets.remove(bullet)
        target, collisionResultData = collisionResult
        if target == BulletCollisionTarget.construction:
            self.processConstructionCollision(bullet, collisionResultData)
        elif target == BulletCollisionTarget.person:
            self.processPersonCollision(bullet, collisionResultData)

    def processConstructionCollision(self, bullet, collisionResult):
        collisionPoint, frontNormal = collisionResult
        bspTree = self.gameData.visibilityTree
        visibilityLevelSegment = self.traversal.findLevelSegmentOrNone(bspTree, collisionPoint)
        bullet.currentPosition = collisionPoint
        bullet.nextPosition = collisionPoint
        bulletHole = self.bulletHoleFactory.make(collisionPoint, frontNormal, visibilityLevelSegment, bullet.holeInfo)
        self.eventManager.raiseEvent(Events.bulletHoleAdded, bulletHole)

    def processPersonCollision(self, bullet, person):
        person.damage(bullet.damagePercent * PersonConstants.maxPersonHealth)
        print("person health: " + str(person.health))


def makeBulletCollisionProcessor(resolver):
    return BulletCollisionProcessor(
        resolver.resolve(GameData),
        resolver.resolve(BSPTreeTraversal),
        resolver.resolve(BulletCollisionDetector),
        resolver.resolve(BulletHoleFactory),
        resolver.resolve(EventManager),
    )
