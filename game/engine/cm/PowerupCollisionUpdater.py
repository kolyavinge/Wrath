from game.engine.cm.PowerupCollisionDetector import PowerupCollisionDetector
from game.engine.powerup.PowerupProcessor import PowerupProcessor
from game.engine.powerup.PowerupValidator import PowerupValidator
from game.lib.EventManager import EventManager, Events


class PowerupCollisionUpdater:

    def __init__(
        self,
        powerupCollisionDetector: PowerupCollisionDetector,
        powerupValidator: PowerupValidator,
        powerupProcessor: PowerupProcessor,
        eventManager: EventManager,
    ):
        self.powerupCollisionDetector = powerupCollisionDetector
        self.powerupValidator = powerupValidator
        self.powerupProcessor = powerupProcessor
        self.eventManager = eventManager

    def updateForPlayer(self, gameState):
        self.updateForPerson(gameState, gameState.player)

    def updateForEnemies(self, gameState):
        for enemy in gameState.enemies:
            self.updateForPerson(gameState, enemy)

    def updateForPerson(self, gameState, person):
        powerup = self.powerupCollisionDetector.getCollisionResultOrNone(person)
        if powerup is not None and self.powerupValidator.canApply(person, powerup):
            self.powerupProcessor.apply(person, powerup)
            gameState.powerups.remove(powerup)
            powerup.collisionLevelSegment.powerups.remove(powerup)
            powerup.visibilityLevelSegment.powerups.remove(powerup)
            self.eventManager.raiseEvent(Events.powerupPickedUp, (person, powerup))
