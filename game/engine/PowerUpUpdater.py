from game.anx.CommonConstants import CommonConstants
from game.engine.GameData import GameData
from game.engine.PowerupPositionGenerator import PowerupPositionGenerator
from game.lib.List import List
from game.lib.Math import Math
from game.model.powerup.FullHealthPowerup import FullHealthPowerup
from game.model.powerup.HalfHealthPowerup import HalfHealthPowerup
from game.model.powerup.WeaponPowerup import WeaponPowerup


class PowerupUpdater:

    def __init__(self, gameData, positionGenerator):
        self.gameData = gameData
        self.positionGenerator = positionGenerator
        self.delay = 0
        self.powerupCount = {}
        self.powerupCount[WeaponPowerup] = 4
        self.powerupCount[HalfHealthPowerup] = 2
        self.powerupCount[FullHealthPowerup] = 1

    def update(self):
        self.delay = Math.max(self.delay - 1, 0)
        for powerup in self.gameData.powerups:
            powerup.update()

    def generateNew(self):
        if self.delay > 0:
            return

        currentPowerups = self.gameData.powerups
        newPowerups = []
        for powerupType, powerupCount in self.powerupCount.items():
            count = List.count(lambda x: isinstance(x, powerupType), currentPowerups)
            while count < powerupCount:
                powerup = powerupType()
                powerup.position = self.positionGenerator.getPosition(powerup.height)
                newPowerups.append(powerup)
                count += 1

        currentPowerups.extend(newPowerups)
        self.delay = 200 * CommonConstants.mainTimerMsec


def makePowerupUpdater(resolver):
    return PowerupUpdater(resolver.resolve(GameData), resolver.resolve(PowerupPositionGenerator))
