from game.engine.bsp.BSPTreeTraversal import BSPTreeTraversal
from game.engine.cm.BulletCollisionDetector import BulletCollisionDetector
from game.engine.cm.CollidedTarget import CollidedTarget
from game.engine.cm.PersonCollisionDetector import PersonCollisionTarget
from game.engine.person.PersonDamageLogic import PersonDamageLogic
from game.engine.weapon.BulletHoleLogic import BulletHoleLogic
from game.engine.weapon.BulletLogic import BulletLogic
from game.engine.weapon.ExplosionLogic import ExplosionLogic
from game.lib.Random import Random


class BulletCollisionUpdater:

    def __init__(
        self,
        traversal: BSPTreeTraversal,
        bulletCollisionDetector: BulletCollisionDetector,
        bulletHoleLogic: BulletHoleLogic,
        personDamageLogic: PersonDamageLogic,
        bulletLogic: BulletLogic,
        explosionLogic: ExplosionLogic,
    ):
        self.traversal = traversal
        self.bulletCollisionDetector = bulletCollisionDetector
        self.bulletHoleLogic = bulletHoleLogic
        self.personDamageLogic = personDamageLogic
        self.bulletLogic = bulletLogic
        self.explosionLogic = explosionLogic

    def update(self, gameState):
        for bullet in gameState.bullets:
            collisionResult = self.bulletCollisionDetector.getCollisionResultOrNone(bullet, gameState.collisionTree)
            if collisionResult is not None:
                self.processCollision(gameState, bullet, collisionResult)

    def updateForConstructions(self, gameState):
        for bullet in gameState.bullets:
            collisionResult = self.bulletCollisionDetector.getConstructionCollisionResultOrNone(bullet, gameState.collisionTree)
            if collisionResult is not None:
                self.processCollision(gameState, bullet, collisionResult)

    def processCollision(self, gameState, bullet, collisionResult):
        target, collisionResultData = collisionResult
        if target == CollidedTarget.construction:
            self.processConstructionCollision(gameState, bullet, collisionResultData)
        elif target == CollidedTarget.onePerson:
            self.processPersonCollision(gameState, bullet, collisionResultData)
        elif target == CollidedTarget.allPerson:
            for item in collisionResultData:
                self.processPersonCollision(gameState, bullet, item)

    def processConstructionCollision(self, gameState, bullet, collisionResult):
        collisionPoint, construction = collisionResult
        self.moveBulletToCollisionPoint(bullet, collisionPoint, gameState.collisionTree)
        if bullet.ricochetPossibility > 0 and Random.getFloat(0.0, 1.0) <= bullet.ricochetPossibility:
            bullet.direction.reflectBy(construction.frontNormal)
            bullet.velocityValue *= bullet.ricochetVelocityCoeff
            bullet.velocity = bullet.direction.copy()
            bullet.velocity.setLength(bullet.velocityValue)
            bullet.accelValue = 0
            bullet.totalDistance = 0
        else:
            self.bulletLogic.setNotAlive(bullet)
            bullet.damagedObject = construction
            visibilityLevelSegment = self.traversal.findLevelSegment(gameState.visibilityTree, collisionPoint)
            self.explosionLogic.makeExplosion(gameState, bullet)
            self.bulletHoleLogic.makeHole(gameState, collisionPoint, construction.frontNormal, visibilityLevelSegment, bullet.holeInfo)

    def processPersonCollision(self, gameState, bullet, collisionResult):
        collisionPoint, person, target = collisionResult
        bullet.damagedObject = person
        if bullet.goThroughPerson:
            if person not in bullet.damagedPersonSet:
                self.personDamageLogic.damageByBullet(person, gameState.allPersonItems[person], bullet, gameState.collisionData)
                bullet.damagedPersonSet.add(person)  # one person damaged only once
        else:
            self.bulletLogic.setNotAlive(bullet)
            self.moveBulletToCollisionPoint(bullet, collisionPoint, gameState.collisionTree)
            if bullet.isHeadshotEnabled and target == PersonCollisionTarget.head:
                self.personDamageLogic.damageByHeadshot(person, bullet, gameState.collisionData)
            else:
                self.personDamageLogic.damageByBullet(person, gameState.allPersonItems[person], bullet, gameState.collisionData)
        if bullet.paralyze and person.health > 0:
            person.paralyzeDelay.set(bullet.paralyzeTime)
        self.explosionLogic.makeExplosion(gameState, bullet)

    def moveBulletToCollisionPoint(self, bullet, collisionPoint, collisionTree):
        bullet.currentPosition = collisionPoint
        bullet.nextPosition = collisionPoint
        levelSegment = self.traversal.findLevelSegment(collisionTree, collisionPoint)
        bullet.currentLevelSegment = levelSegment
        bullet.nextLevelSegment = levelSegment
