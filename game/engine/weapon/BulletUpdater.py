class BulletUpdater:

    def update(self, gameState):
        for bullet in gameState.bullets:
            bullet.update()

    def removeNotAlive(self, gameState):
        if len(gameState.bulletsToRemove) == 0:
            return

        for bulletToRemove in gameState.bulletsToRemove:
            gameState.bullets.remove(bulletToRemove)
            if bulletToRemove.isVisible:
                bulletToRemove.currentVisibilityLevelSegment.bullets.remove(bulletToRemove)

        gameState.bulletsToRemove.clear()
