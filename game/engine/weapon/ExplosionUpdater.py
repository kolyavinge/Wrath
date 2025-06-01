from game.engine.GameData import GameData
from game.engine.weapon.ExplosionLogic import ExplosionLogic


class ExplosionUpdater:

    def __init__(
        self,
        gameData: GameData,
        explosionLogic: ExplosionLogic,
    ):
        self.gameData = gameData
        self.explosionLogic = explosionLogic

    def update(self):
        for explosion in self.gameData.explosions:
            explosion.update()
            if not explosion.isVisible:
                self.explosionLogic.removeExplosion(explosion)
