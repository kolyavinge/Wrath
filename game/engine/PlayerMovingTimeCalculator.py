from game.engine.GameData import GameData
from game.model.person.PersonState import PersonState


class PlayerMovingTimeCalculator:

    def __init__(self, gameData):
        self.gameData = gameData

    def calculate(self):
        for person, inputData in self.gameData.allPersonInputData.items():
            self.calculateForPerson(person, inputData)

    def calculateForPerson(self, person, inputData):
        personStand = person.state == PersonState.standing

        if inputData.goForward and personStand:
            person.forwardMovingTime = self.limitTo(person.forwardMovingTime + person.movingTimeDelta, 1.25)
        else:
            person.forwardMovingTime = self.limitBy(person.forwardMovingTime * 0.8, 0.1, 0)

        if inputData.goBackward and personStand:
            person.backwardMovingTime = self.limitTo(person.backwardMovingTime + person.movingTimeDelta, 0.5)
        else:
            person.backwardMovingTime = self.limitBy(person.backwardMovingTime * 0.8, 0.1, 0)

        if inputData.stepLeft and personStand:
            person.leftStepMovingTime = self.limitTo(person.leftStepMovingTime + person.movingTimeDelta, 0.5)
        else:
            person.leftStepMovingTime = self.limitBy(person.leftStepMovingTime * 0.8, 0.1, 0)

        if inputData.stepRight and personStand:
            person.rightStepMovingTime = self.limitTo(person.rightStepMovingTime + person.movingTimeDelta, 0.5)
        else:
            person.rightStepMovingTime = self.limitBy(person.rightStepMovingTime * 0.8, 0.1, 0)

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
