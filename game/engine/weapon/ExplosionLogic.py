from game.anx.ExplosionIdLogic import ExplosionIdLogic
from game.engine.weapon.DebrisLogic import DebrisLogic
from game.lib.EventManager import EventManager, Events


class ExplosionLogic:

    def __init__(
        self,
        debrisLogic: DebrisLogic,
        explosionIdLogic: ExplosionIdLogic,
        eventManager: EventManager,
    ):
        self.debrisLogic = debrisLogic
        self.explosionIdLogic = explosionIdLogic
        self.eventManager = eventManager

    def makeExplosion(self, gameState, bullet, id=None):
        explosion = bullet.makeExplosion()
        if explosion is not None:
            explosion.id = id or self.explosionIdLogic.getExplosionId()
            explosion.collisionLevelSegment = bullet.currentLevelSegment
            explosion.visibilityLevelSegment = bullet.currentVisibilityLevelSegment
            explosion.collisionLevelSegment.explosions.append(explosion)
            explosion.visibilityLevelSegment.explosions.append(explosion)
            explosion.initTimeSec = gameState.globalTimeSec
            gameState.explosions.append(explosion)
            self.debrisLogic.makeDebrisFromExplosion(gameState, explosion)
            self.eventManager.raiseEvent(Events.exploded, explosion)

    def removeExplosion(self, gameState, explosion):
        explosion.collisionLevelSegment.explosions.remove(explosion)
        explosion.visibilityLevelSegment.explosions.remove(explosion)
        gameState.explosions.remove(explosion)
