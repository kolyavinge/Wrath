from game.engine.GameState import GameState
from game.engine.weapon.BulletLogic import BulletLogic
from game.lib.EventManager import EventManager, Events


class ExplosionLogic:

    def __init__(
        self,
        gameData: GameState,
        bulletLogic: BulletLogic,
        eventManager: EventManager,
    ):
        self.gameData = gameData
        self.bulletLogic = bulletLogic
        self.eventManager = eventManager

    def makeExplosion(self, bullet):
        explosion = bullet.makeExplosion()
        if explosion is not None:
            explosion.collisionLevelSegment = bullet.currentLevelSegment
            explosion.visibilityLevelSegment = bullet.currentVisibilityLevelSegment
            explosion.collisionLevelSegment.explosions.append(explosion)
            explosion.visibilityLevelSegment.explosions.append(explosion)
            explosion.initTimeSec = self.gameData.globalTimeSec
            self.gameData.explosions.append(explosion)
            self.bulletLogic.makeDebris(explosion)
            self.eventManager.raiseEvent(Events.exploded, explosion)

    def removeExplosion(self, explosion):
        explosion.collisionLevelSegment.explosions.remove(explosion)
        explosion.visibilityLevelSegment.explosions.remove(explosion)
        self.gameData.explosions.remove(explosion)
