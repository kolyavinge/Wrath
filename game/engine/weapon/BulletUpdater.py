from game.anx.CommonConstants import CommonConstants
from game.calc.Vector3 import Vector3
from game.engine.cm.ConstructionCollisionDetector import ConstructionCollisionDetector
from game.engine.weapon.BulletHoleLogic import BulletHoleLogic
from game.engine.weapon.BulletLogic import BulletLogic
from game.engine.weapon.ExplosionLogic import ExplosionLogic
from game.lib.IdList import IdList
from game.model.weapon.Grenade import Grenade


class BulletUpdater:

    def __init__(
        self,
        bulletLogic: BulletLogic,
        explosionLogic: ExplosionLogic,
        bulletHoleLogic: BulletHoleLogic,
        constructionCollisionDetector: ConstructionCollisionDetector,
    ):
        self.bulletLogic = bulletLogic
        self.explosionLogic = explosionLogic
        self.bulletHoleLogic = bulletHoleLogic
        self.constructionCollisionDetector = constructionCollisionDetector

    def update(self, gameState):
        for bullet in gameState.bullets:
            bullet.update()

    def updateGrenadesDetonationTimeout(self, gameState):
        for grenade in gameState.bullets:
            if not isinstance(grenade, Grenade):
                continue
            grenade.detonationTimeout.decrease()
            if grenade.detonationTimeout.isExpired():
                self.bulletLogic.setNotAlive(grenade)
                self.explosionLogic.makeExplosion(gameState, grenade)
                layOnFloor = self.constructionCollisionDetector.getCollidedConstructionOrNone(
                    grenade.currentLevelSegment.floors,
                    grenade.currentPosition,
                    Vector3(grenade.currentPosition.x, grenade.currentPosition.y, grenade.currentPosition.z - CommonConstants.minBulletVelocityValue),
                )
                if layOnFloor is not None:
                    self.bulletHoleLogic.makeHole(
                        gameState, grenade.currentPosition, layOnFloor.frontNormal, grenade.currentVisibilityLevelSegment, grenade.holeInfo
                    )

    def updateNotAliveBullets(self, gameState):
        hasRemovedBullets = False
        for removedBullet in gameState.bullets:
            if not removedBullet.isAlive:
                gameState.removedBullets.append(removedBullet)
                self.bulletLogic.removeFromVisibilityLevelSegment(removedBullet)
                hasRemovedBullets = True
        if hasRemovedBullets:
            gameState.bullets = IdList([bullet for bullet in gameState.bullets if bullet.isAlive])
