from game.engine.weapon.BulletLogic import BulletLogic
from game.engine.weapon.ExplosionLogic import ExplosionLogic
from game.lib.IdList import IdList
from game.model.weapon.Grenade import Grenade


class BulletUpdater:

    def __init__(
        self,
        bulletLogic: BulletLogic,
        explosionLogic: ExplosionLogic,
    ):
        self.bulletLogic = bulletLogic
        self.explosionLogic = explosionLogic

    def update(self, gameState):
        for bullet in gameState.bullets:
            bullet.update()

    def updateGrenadesDetonationTimeout(self, gameState):
        for grenade in gameState.bullets:
            if isinstance(grenade, Grenade):
                grenade.detonationTimeout.decrease()
                if grenade.detonationTimeout.isExpired():
                    self.bulletLogic.setNotAlive(grenade)
                    self.explosionLogic.makeExplosion(gameState, grenade)

    def updateNotAliveBullets(self, gameState):
        hasRemovedBullets = False
        for removedBullet in gameState.bullets:
            if not removedBullet.isAlive:
                gameState.removedBullets.append(removedBullet)
                self.bulletLogic.removeFromVisibilityLevelSegment(removedBullet)
                hasRemovedBullets = True
        if hasRemovedBullets:
            gameState.bullets = IdList([bullet for bullet in gameState.bullets if bullet.isAlive])
