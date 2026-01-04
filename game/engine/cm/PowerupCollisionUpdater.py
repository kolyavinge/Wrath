from game.engine.cm.PowerupCollisionDetector import PowerupCollisionDetector
from game.engine.GameState import GameState
from game.engine.powerup.PowerupProcessor import PowerupProcessor
from game.engine.powerup.PowerupValidator import PowerupValidator
from game.lib.EventManager import EventManager, Events


class PowerupCollisionUpdater:

    def __init__(
        self,
        gameState: GameState,
        powerupCollisionDetector: PowerupCollisionDetector,
        powerupValidator: PowerupValidator,
        powerupProcessor: PowerupProcessor,
        eventManager: EventManager,
    ):
        self.gameState = gameState
        self.powerupCollisionDetector = powerupCollisionDetector
        self.powerupValidator = powerupValidator
        self.powerupProcessor = powerupProcessor
        self.eventManager = eventManager

    def update(self):
        for person in self.gameState.allPerson:
            self.updateForPerson(person)

    def updateForPerson(self, person):
        powerup = self.powerupCollisionDetector.getCollisionResultOrNone(person)
        if powerup is not None and self.powerupValidator.canApply(person, powerup):
            self.powerupProcessor.apply(person, powerup)
            self.gameState.powerups.remove(powerup)
            powerup.collisionLevelSegment.powerups.remove(powerup)
            powerup.visibilityLevelSegment.powerups.remove(powerup)
            self.eventManager.raiseEvent(Events.powerupPickedUp, (person, powerup))
