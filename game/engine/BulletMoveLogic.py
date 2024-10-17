from game.anx.CommonConstants import CommonConstants
from game.engine.GameData import GameData


class BulletMoveLogic:

    def __init__(self, gameData):
        self.gameData = gameData

    def process(self):
        for bullet in self.gameData.bullets:
            self.moveBullet(bullet)

    def moveBullet(self, bullet):
        bullet.totalDistance += bullet.velocityValue
        if bullet.totalDistance < CommonConstants.maxLevelSize:
            bullet.nextPosition.add(bullet.velocity)
        else:
            self.gameData.bullets.remove(bullet)


def makeBulletMoveLogic(resolver):
    return BulletMoveLogic(resolver.resolve(GameData))
