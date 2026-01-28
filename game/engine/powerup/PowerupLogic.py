from game.anx.PowerupIdLogic import PowerupIdLogic
from game.engine.bsp.BSPTreeTraversal import BSPTreeTraversal


class PowerupLogic:

    def __init__(
        self,
        powerupIdLogic: PowerupIdLogic,
        traversal: BSPTreeTraversal,
    ):
        self.powerupIdLogic = powerupIdLogic
        self.traversal = traversal

    def makePowerup(self, gameState, powerupType, position, id=None):
        powerup = powerupType()
        powerup.id = id or self.powerupIdLogic.getPowerupId()
        powerup.setPosition(position)
        gameState.powerups.append(powerup)

        levelSegment = self.traversal.findLevelSegmentOrNone(gameState.collisionTree, powerup.position)
        levelSegment.powerups.append(powerup)
        powerup.collisionLevelSegment = levelSegment

        levelSegment = self.traversal.findLevelSegmentOrNone(gameState.visibilityTree, powerup.position)
        levelSegment.powerups.append(powerup)
        powerup.visibilityLevelSegment = levelSegment

        return powerup

    def removePowerup(self, gameState, powerup):
        gameState.powerups.remove(powerup)
        powerup.collisionLevelSegment.powerups.remove(powerup)
        powerup.visibilityLevelSegment.powerups.remove(powerup)
