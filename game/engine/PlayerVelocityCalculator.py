from game.anx.CommonConstants import CommonConstants
from game.calc.Geometry import Geometry
from game.engine.GameData import GameData
from game.lib.Math import Math


class PlayerVelocityCalculator:

    def __init__(self, gameData):
        self.gameData = gameData

    def calculate(self):
        inputData = self.gameData.playerInputData
        player = self.gameData.player

        if inputData.goForward:
            player.forwardMovingTime += player.movingTimeDelta
            if player.forwardMovingTime > player.velocityFunc.forwardMaxTime:
                player.forwardMovingTime = player.velocityFunc.forwardMaxTime
        elif inputData.goBackward:
            player.backwardMovingTime += player.movingTimeDelta
            if player.backwardMovingTime > player.velocityFunc.backwardMaxTime:
                player.backwardMovingTime = player.velocityFunc.backwardMaxTime
        else:
            player.forwardMovingTime *= 0.8
            if player.forwardMovingTime < 0.1:
                player.forwardMovingTime = 0
            player.backwardMovingTime *= 0.8
            if player.backwardMovingTime < 0.1:
                player.backwardMovingTime = 0

        totalMovingTime = player.forwardMovingTime - player.backwardMovingTime
        player.velocityValue = player.velocityFunc.getValue(Math.abs(totalMovingTime))

        if totalMovingTime != 0:
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
        else:
            if inputData.stepLeft or inputData.stepRight:
                player.velocityValue = player.velocityFunc.getValue(0.4)
                player.velocityVector = player.rightNormal.copy()
                player.velocityVector.setLength(player.velocityValue)
                if inputData.stepLeft:
                    player.velocityVector.mul(-1)


def makePlayerVelocityCalculator(resolver):
    return PlayerVelocityCalculator(resolver.resolve(GameData))
