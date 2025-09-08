from game.anx.CommonConstants import CommonConstants
from game.calc.Geometry import Geometry
from game.engine.GameData import GameData
from game.lib.Math import Math
from game.model.person.PersonStates import PersonZState


class PersonVelocityUpdater:

    def __init__(self, gameData: GameData):
        self.gameData = gameData

    def update(self):
        for person in self.gameData.allPerson:
            self.updateForPerson(person)

    def updateForPerson(self, person):
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
        self.slowdownIfNeeded(person)
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
        self.slowdownIfNeeded(person)
        person.velocityVector = person.rightNormal.copy()
        person.velocityVector.setLength(person.velocityValue)
        if movingTime < 0:
            person.velocityVector.mul(-1)

    def slowdownIfNeeded(self, person):
        if person.zState == PersonZState.onFloor:
            person.velocityValue *= person.currentFloor.slowdownCoeff
            person.velocityValue *= self.gameData.allPersonItems[person].currentWeapon.slowdownCoeff
