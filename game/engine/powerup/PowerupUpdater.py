from game.anx.CommonConstants import CommonConstants
from game.engine.bsp.BSPTreeTraversal import BSPTreeTraversal
from game.engine.GameData import GameData
from game.engine.powerup.PowerupPositionGenerator import PowerupPositionGenerator
from game.lib.Math import Math
from game.lib.Query import Query
from game.model.powerup.LargeHealthPowerup import LargeHealthPowerup
from game.model.powerup.SmallHealthPowerup import SmallHealthPowerup
from game.model.powerup.VestPowerup import VestPowerup
from game.model.powerup.WeaponPowerup import WeaponPowerup


class PowerupUpdater:

    def __init__(
        self,
        gameData: GameData,
        positionGenerator: PowerupPositionGenerator,
        traversal: BSPTreeTraversal,
    ):
        self.gameData = gameData
        self.positionGenerator = positionGenerator
        self.traversal = traversal
        self.delay = 0
        self.powerupCount = {}
        self.powerupCount[WeaponPowerup] = 8
        self.powerupCount[SmallHealthPowerup] = 4
        self.powerupCount[LargeHealthPowerup] = 2
        self.powerupCount[VestPowerup] = 2

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
            count = Query(currentPowerups).count(lambda x: isinstance(x, powerupType))
            while count < powerupCount:
                powerup = self.makeNewPowerup(powerupType)
                newPowerups.append(powerup)
                count += 1

        currentPowerups.extend(newPowerups)
        self.delay = 200 * CommonConstants.mainTimerMsec

    def makeNewPowerup(self, powerupType):
        powerup = powerupType()
        powerup.setPosition(self.positionGenerator.getPosition())

        levelSegment = self.traversal.findLevelSegmentOrNone(self.gameData.collisionTree, powerup.position)
        levelSegment.powerups.append(powerup)
        powerup.collisionLevelSegment = levelSegment

        levelSegment = self.traversal.findLevelSegmentOrNone(self.gameData.visibilityTree, powerup.position)
        levelSegment.powerups.append(powerup)
        powerup.visibilityLevelSegment = levelSegment

        return powerup


def makePowerupUpdater(resolver):
    return PowerupUpdater(
        resolver.resolve(GameData),
        resolver.resolve(PowerupPositionGenerator),
        resolver.resolve(BSPTreeTraversal),
    )
