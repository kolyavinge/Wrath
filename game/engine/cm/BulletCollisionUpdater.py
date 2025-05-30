from game.anx.Events import Events
from game.engine.bsp.BSPTreeTraversal import BSPTreeTraversal
from game.engine.cm.BulletCollisionDetector import *
from game.engine.GameData import GameData
from game.engine.person.PersonDamageLogic import PersonDamageLogic
from game.engine.weapon.BulletHoleFactory import BulletHoleFactory
from game.lib.EventManager import EventManager


class BulletCollisionUpdater:

    def __init__(
        self,
        gameData: GameData,
        traversal: BSPTreeTraversal,
        bulletCollisionDetector: BulletCollisionDetector,
        bulletHoleFactory: BulletHoleFactory,
        personDamageLogic: PersonDamageLogic,
        eventManager: EventManager,
    ):
        self.gameData = gameData
        self.traversal = traversal
        self.bulletCollisionDetector = bulletCollisionDetector
        self.bulletHoleFactory = bulletHoleFactory
        self.personDamageLogic = personDamageLogic
        self.eventManager = eventManager

    def update(self):
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

    def processPersonCollision(self, bullet, collisionResult):
        collisionPoint, person = collisionResult
        bullet.currentPosition = collisionPoint
        bullet.nextPosition = collisionPoint
        self.personDamageLogic.damageByBullet(person, bullet)
