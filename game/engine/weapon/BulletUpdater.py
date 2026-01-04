from game.engine.GameState import GameState


class BulletUpdater:

    def __init__(self, gameState: GameState):
        self.gameState = gameState

    def update(self):
        for bullet in self.gameState.bullets:
            bullet.update()

    def removeNotAlive(self):
        if len(self.gameState.bulletsToRemove) == 0:
            return

        for bulletToRemove in self.gameState.bulletsToRemove:
            self.gameState.bullets.remove(bulletToRemove)
            if bulletToRemove.isVisible:
                bulletToRemove.currentVisibilityLevelSegment.bullets.remove(bulletToRemove)

        self.gameState.bulletsToRemove.clear()
