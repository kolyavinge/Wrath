from game.engine.GameState import GameState
from game.engine.weapon.BulletLogic import BulletLogic
from game.engine.weapon.ExplosionLogic import ExplosionLogic
from game.model.weapon.Weapon import FireState


class LauncherAltFireLogic:

    def __init__(
        self,
        gameData: GameState,
        bulletLogic: BulletLogic,
        explosionLogic: ExplosionLogic,
    ):
        self.gameData = gameData
        self.bulletLogic = bulletLogic
        self.explosionLogic = explosionLogic

    def apply(self, person, personItems, weapon):
        if weapon.altFireState == FireState.activated:
            personBullets = [bullet for bullet in self.gameData.bullets if bullet.ownerPerson == person]
            for bullet in personBullets:
                self.explosionLogic.makeExplosion(bullet)
                self.bulletLogic.removeBullet(bullet)
