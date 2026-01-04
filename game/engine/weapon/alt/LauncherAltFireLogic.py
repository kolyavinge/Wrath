from game.engine.GameState import GameState
from game.engine.weapon.BulletLogic import BulletLogic
from game.engine.weapon.ExplosionLogic import ExplosionLogic
from game.model.weapon.Weapon import FireState


class LauncherAltFireLogic:

    def __init__(
        self,
        gameState: GameState,
        bulletLogic: BulletLogic,
        explosionLogic: ExplosionLogic,
    ):
        self.gameState = gameState
        self.bulletLogic = bulletLogic
        self.explosionLogic = explosionLogic

    def apply(self, person, personItems, weapon):
        if weapon.altFireState == FireState.activated:
            personBullets = [bullet for bullet in self.gameState.bullets if bullet.ownerPerson == person]
            for bullet in personBullets:
                self.explosionLogic.makeExplosion(bullet)
                self.bulletLogic.removeBullet(bullet)
