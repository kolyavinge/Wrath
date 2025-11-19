from game.engine.GameData import GameData


class ExplosionLogic:

    def __init__(self, gameData: GameData):
        self.gameData = gameData

    def makeExplosion(self, bullet):
        explosion = bullet.makeExplosion()
        if explosion is not None:
            explosion.collisionLevelSegment = bullet.currentLevelSegment
            explosion.visibilityLevelSegment = bullet.currentVisibilityLevelSegment
            explosion.collisionLevelSegment.explosions.append(explosion)
            explosion.visibilityLevelSegment.explosions.append(explosion)
            explosion.initTimeSec = self.gameData.globalTimeSec
            self.gameData.explosions.append(explosion)

    def removeExplosion(self, explosion):
        explosion.collisionLevelSegment.explosions.remove(explosion)
        explosion.visibilityLevelSegment.explosions.remove(explosion)
        self.gameData.explosions.remove(explosion)
