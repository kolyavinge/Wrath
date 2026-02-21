from game.anx.PowerupIdLogic import PowerupIdLogic
from game.engine.bsp.BSPTreeTraversal import BSPTreeTraversal
from game.model.powerup.PowerupType import PowerupType


class PowerupLogic:

    def __init__(
        self,
        powerupIdLogic: PowerupIdLogic,
        traversal: BSPTreeTraversal,
    ):
        self.powerupIdLogic = powerupIdLogic
        self.traversal = traversal

    def makePowerup(self, gameState, powerupType, position):
        powerup = powerupType()
        powerup.id = self.powerupIdLogic.getPowerupId()
        powerup.setPosition(position)
        gameState.powerups.append(powerup)
        self.initLevelSegments(gameState, powerup)

        return powerup

    def makePowerupFromKind(self, gameState, id, kind, position):
        powerupType = PowerupType.getPowerupTypeFromKind(kind)
        powerup = powerupType(kind)
        powerup.id = id
        powerup.setPosition(position)
        gameState.powerups.append(powerup)
        self.initLevelSegments(gameState, powerup)

        return powerup

    def initLevelSegments(self, gameState, powerup):
        levelSegment = self.traversal.findLevelSegment(gameState.collisionTree, powerup.position)
        levelSegment.powerups.append(powerup)
        powerup.collisionLevelSegment = levelSegment

        levelSegment = self.traversal.findLevelSegment(gameState.visibilityTree, powerup.position)
        levelSegment.powerups.append(powerup)
        powerup.visibilityLevelSegment = levelSegment

    def removePowerup(self, gameState, powerup):
        gameState.powerups.remove(powerup)
        powerup.collisionLevelSegment.powerups.remove(powerup)
        powerup.visibilityLevelSegment.powerups.remove(powerup)
