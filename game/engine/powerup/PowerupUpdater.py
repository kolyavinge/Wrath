from game.anx.CommonConstants import CommonConstants
from game.anx.PowerupIdLogic import PowerupIdLogic
from game.engine.bsp.BSPTreeTraversal import BSPTreeTraversal
from game.engine.powerup.PowerupPositionGenerator import PowerupPositionGenerator
from game.lib.DecrementCounter import DecrementCounter
from game.lib.Query import Query
from game.model.powerup.LargeHealthPowerup import LargeHealthPowerup
from game.model.powerup.SmallHealthPowerup import SmallHealthPowerup
from game.model.powerup.VestPowerup import VestPowerup
from game.model.powerup.WeaponPowerup import WeaponPowerup


class PowerupUpdater:

    def __init__(
        self,
        positionGenerator: PowerupPositionGenerator,
        traversal: BSPTreeTraversal,
        powerupIdLogic: PowerupIdLogic,
    ):
        self.positionGenerator = positionGenerator
        self.traversal = traversal
        self.powerupIdLogic = powerupIdLogic
        self.delay = DecrementCounter()
        self.powerupCount = {}
        self.powerupCount[WeaponPowerup] = 8
        self.powerupCount[SmallHealthPowerup] = 4
        self.powerupCount[LargeHealthPowerup] = 2
        self.powerupCount[VestPowerup] = 2

    def update(self, gameState):
        self.delay.decrease()
        for powerup in gameState.powerups:
            powerup.update()

    def generateNew(self, gameState):
        if not self.delay.isExpired():
            return

        currentPowerups = gameState.powerups
        newPowerups = []
        for powerupType, powerupCount in self.powerupCount.items():
            count = Query(currentPowerups).count(lambda x: type(x) == powerupType)
            while count < powerupCount:
                powerup = self.makeNewPowerup(gameState, powerupType)
                newPowerups.append(powerup)
                count += 1

        currentPowerups.extend(newPowerups)
        self.delay.set(200 * CommonConstants.mainTimerMsec)

    def makeNewPowerup(self, gameState, powerupType):
        powerup = powerupType()
        powerup.id = self.powerupIdLogic.getPowerupId()
        powerup.setPosition(self.positionGenerator.getPosition(gameState))

        levelSegment = self.traversal.findLevelSegmentOrNone(gameState.collisionTree, powerup.position)
        levelSegment.powerups.append(powerup)
        powerup.collisionLevelSegment = levelSegment

        levelSegment = self.traversal.findLevelSegmentOrNone(gameState.visibilityTree, powerup.position)
        levelSegment.powerups.append(powerup)
        powerup.visibilityLevelSegment = levelSegment

        return powerup
