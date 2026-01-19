from game.engine.weapon.ExplosionLogic import ExplosionLogic


class ExplosionUpdater:

    def __init__(
        self,
        explosionLogic: ExplosionLogic,
    ):
        self.explosionLogic = explosionLogic

    def update(self, gameState):
        for explosion in gameState.explosions:
            explosion.update()
            if not explosion.isVisible:
                self.explosionLogic.removeExplosion(gameState, explosion)
