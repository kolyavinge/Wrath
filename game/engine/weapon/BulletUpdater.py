from game.engine.weapon.BulletLogic import BulletLogic
from game.lib.IdList import IdList


class BulletUpdater:

    def __init__(
        self,
        bulletLogic: BulletLogic,
    ):
        self.bulletLogic = bulletLogic

    def update(self, gameState):
        for bullet in gameState.bullets:
            bullet.update()

    def updateNotAliveBullets(self, gameState):
        hasRemovedBullets = False
        for removedBullet in gameState.bullets:
            if not removedBullet.isAlive:
                gameState.removedBullets.append(removedBullet)
                self.bulletLogic.removeFromVisibilityLevelSegment(removedBullet)
                hasRemovedBullets = True
        if hasRemovedBullets:
            gameState.bullets = IdList([bullet for bullet in gameState.bullets if bullet.isAlive])
