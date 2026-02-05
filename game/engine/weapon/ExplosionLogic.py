from game.engine.weapon.DebrisLogic import DebrisLogic


class ExplosionLogic:

    def __init__(
        self,
        debrisLogic: DebrisLogic,
    ):
        self.debrisLogic = debrisLogic

    def makeExplosion(self, gameState, bullet):
        explosion = bullet.makeExplosion()
        if explosion is not None:
            explosion.collisionLevelSegment = bullet.currentLevelSegment
            explosion.visibilityLevelSegment = bullet.currentVisibilityLevelSegment
            explosion.collisionLevelSegment.explosions.append(explosion)
            explosion.visibilityLevelSegment.explosions.append(explosion)
            explosion.initTimeSec = gameState.globalTimeSec
            gameState.explosions.append(explosion)
            self.debrisLogic.makeDebrisFromExplosion(gameState, explosion)
            gameState.updateStatistic.newExplosions.append(explosion)

    def removeExplosion(self, gameState, explosion):
        explosion.collisionLevelSegment.explosions.remove(explosion)
        explosion.visibilityLevelSegment.explosions.remove(explosion)
        gameState.explosions.remove(explosion)
