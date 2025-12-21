from game.engine.GameData import GameData
from game.engine.weapon.BulletLogic import BulletLogic


class ExplosionLogic:

    def __init__(
        self,
        gameData: GameData,
        bulletLogic: BulletLogic,
    ):
        self.gameData = gameData
        self.bulletLogic = bulletLogic

    def makeExplosion(self, bullet):
        explosion = bullet.makeExplosion()
        if explosion is not None:
            explosion.collisionLevelSegment = bullet.currentLevelSegment
            explosion.visibilityLevelSegment = bullet.currentVisibilityLevelSegment
            explosion.collisionLevelSegment.explosions.append(explosion)
            explosion.visibilityLevelSegment.explosions.append(explosion)
            explosion.initTimeSec = self.gameData.globalTimeSec
            self.gameData.explosions.append(explosion)
            self.bulletLogic.makeDebris(explosion)

    def removeExplosion(self, explosion):
        explosion.collisionLevelSegment.explosions.remove(explosion)
        explosion.visibilityLevelSegment.explosions.remove(explosion)
        self.gameData.explosions.remove(explosion)
