from game.engine.GameData import GameData
from game.engine.weapon.BulletLogic import BulletLogic
from game.engine.weapon.ExplosionLogic import ExplosionLogic
from game.model.person.PersonInputData import FireState


class LauncherAltFireLogic:

    def __init__(
        self,
        gameData: GameData,
        bulletLogic: BulletLogic,
        explosionLogic: ExplosionLogic,
    ):
        self.gameData = gameData
        self.bulletLogic = bulletLogic
        self.explosionLogic = explosionLogic

    def apply(self, person, weapon, inputData):
        if inputData.altFireState == FireState.activated:
            personBullets = [bullet for bullet in self.gameData.bullets if bullet.ownerPerson == person]
            for bullet in personBullets:
                self.explosionLogic.makeExplosion(bullet)
                self.bulletLogic.removeBullet(bullet)
