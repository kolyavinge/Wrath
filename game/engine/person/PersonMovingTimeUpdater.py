from game.engine.GameData import GameData
from game.lib.Numeric import Numeric
from game.model.person.PersonZState import PersonZState


class PersonMovingTimeUpdater:

    def __init__(self, gameData: GameData):
        self.gameData = gameData
        self.maxForwardMovingTime = 1.25
        self.maxMovingTime = 0.5
        self.minMovingTimeThreshold = 0.1
        self.movingTimeFade = 0.9

    def update(self):
        for person, inputData in self.gameData.allPersonInputData.items():
            self.updateForPerson(person, inputData)

    def updateForPerson(self, person, inputData):
        if person.zState == PersonZState.onFloor:
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
