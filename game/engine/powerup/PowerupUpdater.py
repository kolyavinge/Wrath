from game.anx.CommonConstants import CommonConstants
from game.engine.powerup.PowerupLogic import PowerupLogic
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
        powerupLogic: PowerupLogic,
    ):
        self.positionGenerator = positionGenerator
        self.powerupLogic = powerupLogic
        self.delay = DecrementCounter()
        self.powerupCount = {}
        self.powerupCount[WeaponPowerup] = 8
        self.powerupCount[SmallHealthPowerup] = 4
        self.powerupCount[LargeHealthPowerup] = 2
        self.powerupCount[VestPowerup] = 2

    def update(self, gameState):
        for powerup in gameState.powerups:
            powerup.update()

    def generateNew(self, gameState):
        self.delay.decrease()
        if not self.delay.isExpired():
            return

        currentPowerups = gameState.powerups
        for powerupType, powerupCount in self.powerupCount.items():
            count = Query(currentPowerups).count(lambda x: type(x) == powerupType)
            while count < powerupCount:
                position = self.positionGenerator.getPosition(gameState)
                self.powerupLogic.makePowerup(gameState, powerupType, position)
                count += 1

        self.delay.set(200 * CommonConstants.mainTimerMsec)
