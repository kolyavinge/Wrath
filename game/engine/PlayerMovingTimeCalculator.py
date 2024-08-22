from game.engine.GameData import GameData


class PlayerMovingTimeCalculator:

    def __init__(self, gameData):
        self.gameData = gameData

    def calculate(self):
        inputData = self.gameData.playerInputData
        player = self.gameData.player

        if inputData.goForward:
            player.forwardMovingTime = self.limitTo(player.forwardMovingTime + player.movingTimeDelta, 1.5)
        else:
            player.forwardMovingTime = self.limitBy(player.forwardMovingTime * 0.8, 0.1, 0)

        if inputData.goBackward:
            player.backwardMovingTime = self.limitTo(player.backwardMovingTime + player.movingTimeDelta, 0.5)
        else:
            player.backwardMovingTime = self.limitBy(player.backwardMovingTime * 0.8, 0.1, 0)

        if inputData.stepLeft:
            player.leftStepMovingTime = self.limitTo(player.leftStepMovingTime + player.movingTimeDelta, 0.5)
        else:
            player.leftStepMovingTime = self.limitBy(player.leftStepMovingTime * 0.8, 0.1, 0)

        if inputData.stepRight:
            player.rightStepMovingTime = self.limitTo(player.rightStepMovingTime + player.movingTimeDelta, 0.5)
        else:
            player.rightStepMovingTime = self.limitBy(player.rightStepMovingTime * 0.8, 0.1, 0)

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


def makePlayerMovingTimeCalculator(resolver):
    return PlayerMovingTimeCalculator(resolver.resolve(GameData))
