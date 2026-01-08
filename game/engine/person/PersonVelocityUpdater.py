from game.anx.CommonConstants import CommonConstants
from game.calc.Geometry import Geometry
from game.engine.GameState import GameState
from game.lib.Math import Math
from game.model.person.PersonStates import PersonZState


class PersonVelocityUpdater:

    def __init__(self, gameState: GameState):
        self.gameState = gameState

    def updateForPlayer(self):
        self.updateForPerson(self.gameState.player)

    def updateForEnemies(self):
        for enemy in self.gameState.enemies:
            self.updateForPerson(enemy)

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

        self.correctByFloor(person)

    def processLeftRightStep(self, person):
        movingTime = person.rightStepMovingTime - person.leftStepMovingTime
        person.velocityValue = person.velocityFunc.getValue(Math.abs(movingTime))
        self.slowdownIfNeeded(person)
        person.velocityVector = person.rightNormal.copy()
        person.velocityVector.setLength(person.velocityValue)
        if movingTime < 0:
            person.velocityVector.mul(-1)
        self.correctByFloor(person)

    def slowdownIfNeeded(self, person):
        if person.zState == PersonZState.onFloor:
            person.velocityValue *= person.currentFloor.slowdownCoeff
            person.velocityValue *= self.gameState.allPersonItems[person].currentWeapon.slowdownCoeff

    def correctByFloor(self, person):
        if not person.currentFloor.isHorizontal and (person.zState == PersonZState.onFloor or person.zState == PersonZState.landing):
            person.velocityVector.add(person.currentCenterPoint)
            person.velocityVector.z = person.currentFloor.getZ(person.velocityVector.x, person.velocityVector.y)
            person.velocityVector.sub(person.currentCenterPoint)
            person.velocityVector.setLength(person.velocityValue)
