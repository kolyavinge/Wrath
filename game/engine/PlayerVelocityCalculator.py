from game.anx.CommonConstants import CommonConstants
from game.calc.Geometry import Geometry
from game.engine.GameData import GameData
from game.lib.Math import Math


class PlayerVelocityCalculator:

    def __init__(self, gameData):
        self.gameData = gameData

    def calculate(self):
        totalMovingTime = self.calculateMovingTime()
        if totalMovingTime != 0:
            self.processForwardBackward(totalMovingTime)
        else:
            self.processLeftRightStep()

    def calculateMovingTime(self):
        inputData = self.gameData.playerInputData
        player = self.gameData.player

        if inputData.goForward:
            player.forwardMovingTime = self.limitTo(player.forwardMovingTime + player.movingTimeDelta, 1.5)
        elif inputData.goBackward:
            player.backwardMovingTime = self.limitTo(player.backwardMovingTime + player.movingTimeDelta, 0.5)
        else:
            player.forwardMovingTime = self.limitBy(player.forwardMovingTime * 0.8, 0.1, 0)
            player.backwardMovingTime = self.limitBy(player.backwardMovingTime * 0.8, 0.1, 0)

        totalMovingTime = player.forwardMovingTime - player.backwardMovingTime
        player.velocityValue = player.velocityFunc.getValue(Math.abs(totalMovingTime))

        return totalMovingTime

    def processForwardBackward(self, totalMovingTime):
        inputData = self.gameData.playerInputData
        player = self.gameData.player

        player.velocityVector = player.frontNormal.copy()
        player.velocityVector.setLength(player.velocityValue)
        if totalMovingTime < 0:
            player.velocityVector.mul(-1)

        radians = 0
        if totalMovingTime > 0 and inputData.stepLeft:
            radians = 0.5
        elif totalMovingTime > 0 and inputData.stepRight:
            radians = -0.5
        elif totalMovingTime < 0 and inputData.stepLeft:
            radians = -0.5
        elif totalMovingTime < 0 and inputData.stepRight:
            radians = 0.5

        if radians != 0:
            player.velocityVector = Geometry.rotatePoint(player.velocityVector, CommonConstants.zAxis, CommonConstants.axisOrigin, radians)

    def processLeftRightStep(self):
        inputData = self.gameData.playerInputData
        player = self.gameData.player

        if inputData.stepLeft or inputData.stepRight:
            player.velocityValue = player.velocityFunc.getValue(0.4)
            player.velocityVector = player.rightNormal.copy()
            player.velocityVector.setLength(player.velocityValue)
            if inputData.stepLeft:
                player.velocityVector.mul(-1)

    def limitTo(self, value, maxValue):
        if value > maxValue:
            return maxValue
        else:
            return value

    def limitBy(self, value, limit, limitedValue):
        if value < limit:
            return limitedValue
        else:
            return value


def makePlayerVelocityCalculator(resolver):
    return PlayerVelocityCalculator(resolver.resolve(GameData))
