from game.engine.GameState import GameState


class BulletUpdater:

    def __init__(self, gameData: GameState):
        self.gameData = gameData

    def update(self):
        for bullet in self.gameData.bullets:
            bullet.update()

    def removeNotAlive(self):
        if len(self.gameData.bulletsToRemove) == 0:
            return

        for bulletToRemove in self.gameData.bulletsToRemove:
            self.gameData.bullets.remove(bulletToRemove)
            if bulletToRemove.isVisible:
                bulletToRemove.currentVisibilityLevelSegment.bullets.remove(bulletToRemove)

        self.gameData.bulletsToRemove.clear()
