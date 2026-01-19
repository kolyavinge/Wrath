from game.engine.weapon.BulletLogic import BulletLogic
from game.lib.EventManager import EventManager, Events


class ExplosionLogic:

    def __init__(
        self,
        bulletLogic: BulletLogic,
        eventManager: EventManager,
    ):
        self.bulletLogic = bulletLogic
        self.eventManager = eventManager

    def makeExplosion(self, gameState, bullet):
        explosion = bullet.makeExplosion()
        if explosion is not None:
            explosion.collisionLevelSegment = bullet.currentLevelSegment
            explosion.visibilityLevelSegment = bullet.currentVisibilityLevelSegment
            explosion.collisionLevelSegment.explosions.append(explosion)
            explosion.visibilityLevelSegment.explosions.append(explosion)
            explosion.initTimeSec = gameState.globalTimeSec
            gameState.explosions.append(explosion)
            self.bulletLogic.makeDebris(gameState, explosion)
            self.eventManager.raiseEvent(Events.exploded, explosion)

    def removeExplosion(self, gameState, explosion):
        explosion.collisionLevelSegment.explosions.remove(explosion)
        explosion.visibilityLevelSegment.explosions.remove(explosion)
        gameState.explosions.remove(explosion)
