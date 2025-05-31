from game.engine.GameData import GameData


class ExplosionLogic:

    def __init__(self, gameData: GameData):
        self.gameData = gameData

    def makeExplosion(self, bullet):
        explosion = bullet.makeExplosion()
        if explosion is not None:
            explosion.levelSegment = bullet.currentLevelSegment
            explosion.visibilityLevelSegment = bullet.currentVisibilityLevelSegment
            self.gameData.explosions.append(explosion)
            explosion.visibilityLevelSegment.explosions.append(explosion)
