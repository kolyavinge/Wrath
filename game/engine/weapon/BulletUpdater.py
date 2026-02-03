class BulletUpdater:

    def update(self, gameState):
        for bullet in gameState.bullets:
            bullet.update()
