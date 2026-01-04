from game.engine.GameState import GameState
from game.engine.weapon.ExplosionLogic import ExplosionLogic


class ExplosionUpdater:

    def __init__(
        self,
        gameData: GameState,
        explosionLogic: ExplosionLogic,
    ):
        self.gameData = gameData
        self.explosionLogic = explosionLogic

    def update(self):
        for explosion in self.gameData.explosions:
            explosion.update()
            if not explosion.isVisible:
                self.explosionLogic.removeExplosion(explosion)
