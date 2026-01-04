from game.engine.GameState import GameState
from game.engine.weapon.ExplosionLogic import ExplosionLogic


class ExplosionUpdater:

    def __init__(
        self,
        gameState: GameState,
        explosionLogic: ExplosionLogic,
    ):
        self.gameState = gameState
        self.explosionLogic = explosionLogic

    def update(self):
        for explosion in self.gameState.explosions:
            explosion.update()
            if not explosion.isVisible:
                self.explosionLogic.removeExplosion(explosion)
