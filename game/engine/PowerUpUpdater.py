from game.anx.CommonConstants import CommonConstants
from game.calc.Vector3 import Vector3
from game.engine.bsp.BSPTreeTraversal import BSPTreeTraversal
from game.engine.GameData import GameData
from game.engine.PowerupPositionGenerator import PowerupPositionGenerator
from game.lib.List import List
from game.lib.Math import Math
from game.model.powerup.FullHealthPowerup import FullHealthPowerup
from game.model.powerup.HalfHealthPowerup import HalfHealthPowerup
from game.model.powerup.WeaponPowerup import WeaponPowerup


class PowerupUpdater:

    def __init__(self, gameData, positionGenerator, traversal):
        self.gameData = gameData
        self.positionGenerator = positionGenerator
        self.traversal = traversal
        self.delay = 0
        self.powerupCount = {}
        self.powerupCount[WeaponPowerup] = 8
        # self.powerupCount[HalfHealthPowerup] = 2 TODO
        # self.powerupCount[FullHealthPowerup] = 1 TODO

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
                powerup = self.makeNewPowerup(powerupType)
                newPowerups.append(powerup)
                count += 1

        currentPowerups.extend(newPowerups)
        self.delay = 200 * CommonConstants.mainTimerMsec

    def makeNewPowerup(self, powerupType):
        powerup = powerupType()
        powerup.position = self.positionGenerator.getPosition(powerup.height)
        levelSegment = self.traversal.findLevelSegmentOrNone(self.gameData.level.collisionTree, powerup.position)
        levelSegment.powerups.append(powerup)
        levelSegment = self.traversal.findLevelSegmentOrNone(self.gameData.level.visibilityTree, powerup.position)
        levelSegment.powerups.append(powerup)

        return powerup


def makePowerupUpdater(resolver):
    return PowerupUpdater(resolver.resolve(GameData), resolver.resolve(PowerupPositionGenerator), resolver.resolve(BSPTreeTraversal))
