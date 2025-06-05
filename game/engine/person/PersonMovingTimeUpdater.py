from game.engine.GameData import GameData
from game.model.person.PersonZState import PersonZState


class PersonMovingTimeUpdater:

    def __init__(self, gameData: GameData):
        self.gameData = gameData

    def update(self):
        for person, inputData in self.gameData.allPersonInputData.items():
            self.updateForPerson(person, inputData)

    def updateForPerson(self, person, inputData):
        if person.zState != PersonZState.onFloor:
            return

        if inputData.goForward:
            person.forwardMovingTime = self.limitTo(person.forwardMovingTime + person.movingTimeDelta, 1.25)
        else:
            person.forwardMovingTime = self.limitBy(person.forwardMovingTime * 0.9, 0.1, 0)

        if inputData.goBackward:
            person.backwardMovingTime = self.limitTo(person.backwardMovingTime + person.movingTimeDelta, 0.5)
        else:
            person.backwardMovingTime = self.limitBy(person.backwardMovingTime * 0.9, 0.1, 0)

        if inputData.stepLeft:
            person.leftStepMovingTime = self.limitTo(person.leftStepMovingTime + person.movingTimeDelta, 0.5)
        else:
            person.leftStepMovingTime = self.limitBy(person.leftStepMovingTime * 0.9, 0.1, 0)

        if inputData.stepRight:
            person.rightStepMovingTime = self.limitTo(person.rightStepMovingTime + person.movingTimeDelta, 0.5)
        else:
            person.rightStepMovingTime = self.limitBy(person.rightStepMovingTime * 0.9, 0.1, 0)

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
