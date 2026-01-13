from game.engine.bsp.BSPTreeTraversal import BSPTreeTraversal
from game.engine.cm.BulletCollisionDetector import BulletCollisionDetector
from game.engine.cm.CollidedTarget import CollidedTarget
from game.engine.cm.PersonCollisionDetector import PersonCollisionTarget
from game.engine.GameState import GameState
from game.engine.person.PersonDamageLogic import PersonDamageLogic
from game.engine.weapon.BulletHoleLogic import BulletHoleLogic
from game.engine.weapon.BulletLogic import BulletLogic
from game.engine.weapon.ExplosionLogic import ExplosionLogic
from game.lib.Random import Random


class BulletCollisionUpdater:

    def __init__(
        self,
        gameState: GameState,
        traversal: BSPTreeTraversal,
        bulletCollisionDetector: BulletCollisionDetector,
        bulletHoleLogic: BulletHoleLogic,
        personDamageLogic: PersonDamageLogic,
        bulletLogic: BulletLogic,
        explosionLogic: ExplosionLogic,
    ):
        self.gameState = gameState
        self.traversal = traversal
        self.bulletCollisionDetector = bulletCollisionDetector
        self.bulletHoleLogic = bulletHoleLogic
        self.personDamageLogic = personDamageLogic
        self.bulletLogic = bulletLogic
        self.explosionLogic = explosionLogic

    def update(self):
        for bullet in self.gameState.bullets:
            collisionResult = self.bulletCollisionDetector.getCollisionResultOrNone(bullet)
            if collisionResult is not None:
                self.processCollision(bullet, collisionResult)

    def updateForConstructions(self):
        for bullet in self.gameState.bullets:
            collisionResult = self.bulletCollisionDetector.getConstructionCollisionResultOrNone(bullet)
            if collisionResult is not None:
                self.processCollision(bullet, collisionResult)

    def processCollision(self, bullet, collisionResult):
        target, collisionResultData = collisionResult
        if target == CollidedTarget.construction:
            self.processConstructionCollision(bullet, collisionResultData)
        elif target == CollidedTarget.onePerson:
            self.processPersonCollision(bullet, collisionResultData)
        elif target == CollidedTarget.allPerson:
            for item in collisionResultData:
                self.processPersonCollision(bullet, item)
        self.explosionLogic.makeExplosion(bullet)

    def processConstructionCollision(self, bullet, collisionResult):
        collisionPoint, construction = collisionResult
        bullet.currentPosition = collisionPoint
        bullet.nextPosition = collisionPoint
        if bullet.ricochetPossibility > 0 and Random.getFloat(0.0, 1.0) <= bullet.ricochetPossibility:
            bullet.direction.reflectBy(construction.frontNormal)
            bullet.velocityValue /= 2.0
            bullet.velocity = bullet.direction.copy()
            bullet.velocity.setLength(bullet.velocityValue)
            bullet.totalDistance = 0
        else:
            self.bulletLogic.removeBullet(bullet)
            bullet.damagedObject = construction
            bspTree = self.gameState.visibilityTree
            visibilityLevelSegment = self.traversal.findLevelSegmentOrNone(bspTree, collisionPoint)
            self.bulletHoleLogic.makeHole(collisionPoint, construction.frontNormal, visibilityLevelSegment, bullet.holeInfo)

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
