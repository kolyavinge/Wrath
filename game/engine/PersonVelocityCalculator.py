from game.anx.CommonConstants import CommonConstants
from game.calc.Geometry import Geometry
from game.engine.GameData import GameData
from game.lib.Math import Math
from game.model.level.Stair import Stair


class PersonVelocityCalculator:

    def __init__(self, gameData):
        self.gameData = gameData

    def calculate(self):
        for person in self.gameData.allPerson:
            self.calculateForPerson(person)

    def calculateForPerson(self, person):
        person.prevVelocityValue = person.velocityValue
        if person.forwardMovingTime > 0 or person.backwardMovingTime > 0:
            self.processForwardBackward(person)
        elif person.leftStepMovingTime > 0 or person.rightStepMovingTime > 0:
            self.processLeftRightStep(person)
        else:
            person.velocityValue = 0
            person.velocityVector.set(0, 0, 0)

    def processForwardBackward(self, person):
        movingTime = person.forwardMovingTime - person.backwardMovingTime
        person.velocityValue = person.velocityFunc.getValue(Math.abs(movingTime))
        self.slowdownOnStair(person)
        person.velocityVector = person.frontNormal.copy()
        person.velocityVector.setLength(person.velocityValue)
        if movingTime < 0:
            person.velocityVector.mul(-1)

        leftStep = person.leftStepMovingTime > person.rightStepMovingTime
        rightStep = person.leftStepMovingTime < person.rightStepMovingTime
        radians = 0
        if movingTime > 0 and leftStep:
            radians = person.leftStepMovingTime
        elif movingTime > 0 and rightStep:
            radians = -person.rightStepMovingTime
        elif movingTime < 0 and leftStep:
            radians = -person.leftStepMovingTime
        elif movingTime < 0 and rightStep:
            radians = person.rightStepMovingTime

        if radians != 0:
            person.velocityVector = Geometry.rotatePoint(person.velocityVector, CommonConstants.zAxis, CommonConstants.axisOrigin, radians)

    def processLeftRightStep(self, person):
        movingTime = person.rightStepMovingTime - person.leftStepMovingTime
        person.velocityValue = person.velocityFunc.getValue(Math.abs(movingTime))
        self.slowdownOnStair(person)
        person.velocityVector = person.rightNormal.copy()
        person.velocityVector.setLength(person.velocityValue)
        if movingTime < 0:
            person.velocityVector.mul(-1)

    def slowdownOnStair(self, person):
        if isinstance(person.currentFloor, Stair):
            person.velocityValue = Math.min(person.velocityValue, 0.05)


def makePersonVelocityCalculator(resolver):
    return PersonVelocityCalculator(resolver.resolve(GameData))
