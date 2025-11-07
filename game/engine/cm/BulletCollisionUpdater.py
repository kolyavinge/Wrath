from game.engine.bsp.BSPTreeTraversal import BSPTreeTraversal
from game.engine.cm.BulletCollisionDetector import *
from game.engine.cm.PersonCollisionDetector import PersonCollisionTarget
from game.engine.GameData import GameData
from game.engine.person.PersonDamageLogic import PersonDamageLogic
from game.engine.weapon.BulletHoleFactory import BulletHoleFactory
from game.engine.weapon.BulletLogic import BulletLogic
from game.engine.weapon.ExplosionLogic import ExplosionLogic
from game.lib.EventManager import EventManager, Events


class BulletCollisionUpdater:

    def __init__(
        self,
        gameData: GameData,
        traversal: BSPTreeTraversal,
        bulletCollisionDetector: BulletCollisionDetector,
        bulletHoleFactory: BulletHoleFactory,
        personDamageLogic: PersonDamageLogic,
        bulletLogic: BulletLogic,
        explosionLogic: ExplosionLogic,
        eventManager: EventManager,
    ):
        self.gameData = gameData
        self.traversal = traversal
        self.bulletCollisionDetector = bulletCollisionDetector
        self.bulletHoleFactory = bulletHoleFactory
        self.personDamageLogic = personDamageLogic
        self.bulletLogic = bulletLogic
        self.explosionLogic = explosionLogic
        self.eventManager = eventManager

    def update(self):
        for bullet in self.gameData.bullets:
            collisionResult = self.bulletCollisionDetector.getCollisionResultOrNone(bullet)
            if collisionResult is not None:
                self.processCollision(bullet, collisionResult)

    def processCollision(self, bullet, collisionResult):
        target, collisionResultData = collisionResult
        if target == BulletCollisionTarget.construction:
            self.processConstructionCollision(bullet, collisionResultData)
        elif target == BulletCollisionTarget.person:
            self.processPersonCollision(bullet, collisionResultData)
        self.explosionLogic.makeExplosion(bullet)

    def processConstructionCollision(self, bullet, collisionResult):
        self.bulletLogic.removeBullet(bullet)
        collisionPoint, construction = collisionResult
        bullet.damagedObject = construction
        bspTree = self.gameData.visibilityTree
        visibilityLevelSegment = self.traversal.findLevelSegmentOrNone(bspTree, collisionPoint)
        bullet.currentPosition = collisionPoint
        bullet.nextPosition = collisionPoint
        bulletHole = self.bulletHoleFactory.make(collisionPoint, construction.frontNormal, visibilityLevelSegment, bullet.holeInfo)
        self.eventManager.raiseEvent(Events.bulletHoleAdded, bulletHole)

    def processPersonCollision(self, bullet, collisionResult):
        collisionPoint, person, target = collisionResult
        bullet.damagedObject = person
        if bullet.goThroughPerson:
            if person not in bullet.damagedPersonSet:
                self.personDamageLogic.damageByBullet(person, bullet)
                bullet.damagedPersonSet.add(person)  # one person damaged only once
        else:
            self.bulletLogic.removeBullet(bullet)
            bullet.currentPosition = collisionPoint
            bullet.nextPosition = collisionPoint
            if bullet.isHeadshotEnabled and target == PersonCollisionTarget.head:
                self.personDamageLogic.damageByHeadshot(person, bullet)
            else:
                self.personDamageLogic.damageByBullet(person, bullet)
        if bullet.paralyze and person.health > 0:
            person.paralyzeDelay.set(bullet.paralyzeTime)
