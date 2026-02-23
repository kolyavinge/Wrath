class BulletUpdater:

    def update(self, gameState):
        for bullet in gameState.bullets:
            bullet.update()

    def updateNotAliveBullets(self, gameState):
        hasRemovedBullets = False
        for removedBullet in gameState.bullets:
            if not removedBullet.isAlive:
                gameState.removedBullets.append(removedBullet)
                gameState.bullets.remove(removedBullet)
                hasRemovedBullets = True
        if hasRemovedBullets:
            gameState.bullets = [bullet for bullet in gameState.bullets if bullet.isAlive]
