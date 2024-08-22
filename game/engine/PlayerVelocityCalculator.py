from game.anx.CommonConstants import CommonConstants
from game.calc.Geometry import Geometry
from game.engine.GameData import GameData
from game.lib.Math import Math


class PlayerVelocityCalculator:

    def __init__(self, gameData):
        self.gameData = gameData

    def calculate(self):
        player = self.gameData.player
        if player.forwardMovingTime > 0 or player.backwardMovingTime > 0:
            self.processForwardBackward()
        elif player.leftStepMovingTime > 0 or player.rightStepMovingTime > 0:
            self.processLeftRightStep()
        else:
            player.velocityValue = 0

    def processForwardBackward(self):
        player = self.gameData.player

        totalMovingTime = player.forwardMovingTime - player.backwardMovingTime
        player.velocityValue = player.velocityFunc.getValue(Math.abs(totalMovingTime))
        player.velocityVector = player.frontNormal.copy()
        player.velocityVector.setLength(player.velocityValue)
        if totalMovingTime < 0:
            player.velocityVector.mul(-1)

        leftStep = player.leftStepMovingTime > player.rightStepMovingTime
        rightStep = player.leftStepMovingTime < player.rightStepMovingTime
        radians = 0
        if totalMovingTime > 0 and leftStep:
            radians = 0.5
        elif totalMovingTime > 0 and rightStep:
            radians = -0.5
        elif totalMovingTime < 0 and leftStep:
            radians = -0.5
        elif totalMovingTime < 0 and rightStep:
            radians = 0.5

        if radians != 0:
            player.velocityVector = Geometry.rotatePoint(player.velocityVector, CommonConstants.zAxis, CommonConstants.axisOrigin, radians)

    def processLeftRightStep(self):
        player = self.gameData.player
        totalMovingTime = player.rightStepMovingTime - player.leftStepMovingTime
        player.velocityValue = player.velocityFunc.getValue(Math.abs(totalMovingTime))
        player.velocityVector = player.rightNormal.copy()
        player.velocityVector.setLength(player.velocityValue)
        if totalMovingTime < 0:
            player.velocityVector.mul(-1)


def makePlayerVelocityCalculator(resolver):
    return PlayerVelocityCalculator(resolver.resolve(GameData))
