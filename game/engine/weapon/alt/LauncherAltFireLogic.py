from game.engine.weapon.BulletLogic import BulletLogic
from game.engine.weapon.ExplosionLogic import ExplosionLogic
from game.model.weapon.Weapon import FireState


class LauncherAltFireLogic:

    def __init__(
        self,
        bulletLogic: BulletLogic,
        explosionLogic: ExplosionLogic,
    ):
        self.bulletLogic = bulletLogic
        self.explosionLogic = explosionLogic

    def apply(self, gameState, person, personItems, weapon):
        if weapon.altFireState == FireState.activated:
            personBullets = [bullet for bullet in gameState.bullets if bullet.ownerPerson == person]
            for bullet in personBullets:
                self.explosionLogic.makeExplosion(gameState, bullet)
                self.bulletLogic.removeBullet(bullet)
