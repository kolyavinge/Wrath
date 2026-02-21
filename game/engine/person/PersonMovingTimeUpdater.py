from game.lib.Numeric import Numeric


class PersonMovingTimeUpdater:

    def __init__(self):
        self.maxForwardMovingTime = 1.25
        self.maxMovingTime = 0.5
        self.minMovingTimeThreshold = 0.1
        self.movingTimeFade = 0.9

    def updateForPlayer(self, gameState):
        self.updateForPerson(gameState.player, gameState.playerInputData)

    def updateForBots(self, gameState):
        for bot, inputData in gameState.botInputData.items():
            self.updateForPerson(bot, inputData)

    def updateForPerson(self, person, inputData):
        self.updateForwardMovingTime(person, inputData)
        self.updateBackwardMovingTime(person, inputData)
        self.updateLeftStepMovingTime(person, inputData)
        self.updateRightStepMovingTime(person, inputData)

    def updateForwardMovingTime(self, person, inputData):
        if inputData.goForward:
            newMovingTime = person.forwardMovingTime + person.movingTimeDelta
            person.forwardMovingTime = Numeric.limitMax(newMovingTime, self.maxForwardMovingTime, self.maxForwardMovingTime)
        else:
            newMovingTime = person.forwardMovingTime * self.movingTimeFade
            person.forwardMovingTime = Numeric.limitMin(newMovingTime, self.minMovingTimeThreshold, 0)

    def updateBackwardMovingTime(self, person, inputData):
        if inputData.goBackward:
            newMovingTime = person.backwardMovingTime + person.movingTimeDelta
            person.backwardMovingTime = Numeric.limitMax(newMovingTime, self.maxMovingTime, self.maxMovingTime)
        else:
            newMovingTime = person.backwardMovingTime * self.movingTimeFade
            person.backwardMovingTime = Numeric.limitMin(newMovingTime, self.minMovingTimeThreshold, 0)

    def updateLeftStepMovingTime(self, person, inputData):
        if inputData.stepLeft:
            newMovingTime = person.leftStepMovingTime + person.movingTimeDelta
            person.leftStepMovingTime = Numeric.limitMax(newMovingTime, self.maxMovingTime, self.maxMovingTime)
        else:
            newMovingTime = person.leftStepMovingTime * self.movingTimeFade
            person.leftStepMovingTime = Numeric.limitMin(newMovingTime, self.minMovingTimeThreshold, 0)

    def updateRightStepMovingTime(self, person, inputData):
        if inputData.stepRight:
            newMovingTime = person.rightStepMovingTime + person.movingTimeDelta
            person.rightStepMovingTime = Numeric.limitMax(newMovingTime, self.maxMovingTime, self.maxMovingTime)
        else:
            newMovingTime = person.rightStepMovingTime * self.movingTimeFade
            person.rightStepMovingTime = Numeric.limitMin(newMovingTime, self.minMovingTimeThreshold, 0)
