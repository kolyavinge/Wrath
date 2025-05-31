from game.engine.GameData import GameData


class ExplosionUpdater:

    def __init__(self, gameData: GameData):
        self.gameData = gameData

    def update(self):
        for explosion in self.gameData.explosions:
            explosion.update()
            if not explosion.isVisible:
                self.gameData.explosions.remove(explosion)
                explosion.visibilityLevelSegment.explosions.remove(explosion)
