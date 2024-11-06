from game.anx.CommonConstants import CommonConstants
from game.engine.GameData import GameData
from game.engine.PowerUpPositionGenerator import PowerUpPositionGenerator
from game.lib.List import List
from game.lib.Math import Math
from game.model.powerup.FullHealthPowerUp import FullHealthPowerUp
from game.model.powerup.HalfHealthPowerUp import HalfHealthPowerUp
from game.model.powerup.WeaponPowerUp import WeaponPowerUp


class PowerUpUpdater:

    def __init__(self, gameData, positionGenerator):
        self.gameData = gameData
        self.positionGenerator = positionGenerator
        self.delay = 0
        self.powerupCount = {}
        self.powerupCount[WeaponPowerUp] = 4
        self.powerupCount[HalfHealthPowerUp] = 2
        self.powerupCount[FullHealthPowerUp] = 1

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


def makePowerUpUpdater(resolver):
    return PowerUpUpdater(resolver.resolve(GameData), resolver.resolve(PowerUpPositionGenerator))
