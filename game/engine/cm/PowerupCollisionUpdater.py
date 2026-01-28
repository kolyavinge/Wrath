from game.engine.cm.PowerupCollisionDetector import PowerupCollisionDetector
from game.engine.powerup.PowerupLogic import PowerupLogic
from game.engine.powerup.PowerupProcessor import PowerupProcessor
from game.engine.powerup.PowerupValidator import PowerupValidator
from game.lib.EventManager import EventManager, Events


class PowerupCollisionUpdater:

    def __init__(
        self,
        powerupCollisionDetector: PowerupCollisionDetector,
        powerupValidator: PowerupValidator,
        powerupProcessor: PowerupProcessor,
        powerupLogic: PowerupLogic,
        eventManager: EventManager,
    ):
        self.powerupCollisionDetector = powerupCollisionDetector
        self.powerupValidator = powerupValidator
        self.powerupProcessor = powerupProcessor
        self.powerupLogic = powerupLogic
        self.eventManager = eventManager

    def updateForPlayer(self, gameState):
        self.updateForPerson(gameState, gameState.player)

    def updateForEnemies(self, gameState):
        for enemy in gameState.enemies:
            self.updateForPerson(gameState, enemy)

    def updateForPerson(self, gameState, person):
        powerup = self.powerupCollisionDetector.getCollisionResultOrNone(person)
        personItems = gameState.allPersonItems[person]
        if powerup is not None and self.powerupValidator.canApply(person, personItems, powerup):
            self.powerupProcessor.apply(person, personItems, powerup)
            self.powerupLogic.removePowerup(gameState, powerup)
            self.eventManager.raiseEvent(Events.powerupPickedUp, (person, powerup))
