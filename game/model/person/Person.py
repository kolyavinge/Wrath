from game.anx.CommonConstants import CommonConstants
from game.anx.PersonConstants import PersonConstants
from game.calc.Box3d import Box3d
from game.calc.Rect2d import Rect2d
from game.calc.TransformMatrix4Builder import TransformMatrix4Builder
from game.calc.Vector3 import Vector3
from game.lib.DecrementCounter import DecrementCounter
from game.lib.Math import Math
from game.model.level.Floor import Floor
from game.model.level.LevelSegment import LevelSegment
from game.model.person.PersonFuncs import *
from game.model.person.PersonStates import LifeCycle, PersonZState


class Person:

    def __init__(self):
        self.lifeCycle = LifeCycle.alive
        self.lifeCycleDelay = DecrementCounter()
        self.zState = PersonZState.onFloor
        self.prevZState = None
        self.currentCenterPoint = Vector3()
        self.nextCenterPoint = self.currentCenterPoint.copy()
        self.middleCenterPoint = Vector3()
        self.chestCenterPoint = Vector3()
        self.collisionLevelSegments = set()
        self.visibilityLevelSegment = LevelSegment()
        self.currentBorder = Box3d(PersonConstants.xyLength, PersonConstants.xyLength, PersonConstants.zLength)
        self.nextBorder = self.currentBorder.copy()
        self.nextBodyBorder = Box3d(PersonConstants.xyLength, PersonConstants.xyLength, PersonConstants.zChestLength)
        self.currentFootRect = Rect2d(PersonConstants.xyLength, PersonConstants.xyLength)
        self.nextFootRect = Rect2d(PersonConstants.xyLength, PersonConstants.xyLength)
        self.currentFloor = Floor()
        self.nextFloor = Floor()
        self.pitchRadians = 0
        self.yawRadians = 0
        self.eyePosition = Vector3()
        self.lookDirection = CommonConstants.yAxis
        self.lookDirectionNormal = CommonConstants.zAxis
        self.frontNormal = CommonConstants.yAxis
        self.rightNormal = CommonConstants.xAxis
        self.hasMoved = False
        self.hasTurned = False
        self.forwardMovingTime = 0
        self.backwardMovingTime = 0
        self.leftStepMovingTime = 0
        self.rightStepMovingTime = 0
        self.movingTimeDelta = 0.1
        self.prevVelocityValue = 0
        self.velocityValue = 0
        self.velocityVector = Vector3()
        self.velocityFunc = VelocityFunc()
        self.jumpingTime = 0
        self.jumpingValue = 0
        self.jumpingFunc = JumpingFunc()
        self.fallingTime = 0
        self.fallingFunc = FallingFunc()
        self.fallingDamageFunc = FallingDamageFunc()
        self.landingTime = 0
        self.health = PersonConstants.maxPersonHealth
        self.breathTime = 0
        self.breathFunc = BreathFunc()
        self.stepTime = 0
        self.selectWeaponDelay = DecrementCounter()
        self.paralyzeDelay = DecrementCounter()

    def moveNextPositionBy(self, vector):
        self.nextCenterPoint.add(vector)
        self.nextBorder.calculatePointsByCenter(self.nextCenterPoint)
        self.nextBodyBorder.calculatePointsByCenter(self.nextCenterPoint)
        self.nextFootRect.calculatePointsByCenter(self.nextCenterPoint)
        self.nextFootRect.addZ(PersonConstants.zFootLength)

    def moveNextPositionTo(self, vector):
        self.nextCenterPoint = vector
        self.nextBorder.calculatePointsByCenter(self.nextCenterPoint)
        self.nextBodyBorder.calculatePointsByCenter(self.nextCenterPoint)
        self.nextFootRect.calculatePointsByCenter(self.nextCenterPoint)
        self.nextFootRect.addZ(PersonConstants.zFootLength)

    def getZ(self):
        return self.nextCenterPoint.z

    def setZ(self, z):
        self.nextCenterPoint.z = z
        self.nextBorder.calculatePointsByCenter(self.nextCenterPoint)
        self.nextBodyBorder.calculatePointsByCenter(self.nextCenterPoint)
        self.nextFootRect.calculatePointsByCenter(self.nextCenterPoint)
        self.nextFootRect.addZ(PersonConstants.zFootLength)

    def commitNextPosition(self):
        self.currentCenterPoint = self.nextCenterPoint.copy()
        self.currentBorder = self.nextBorder.copy()
        self.eyePosition = self.currentCenterPoint.copy()
        self.eyePosition.z += PersonConstants.eyeLength
        self.middleCenterPoint = self.currentCenterPoint.copy()
        self.middleCenterPoint.z += PersonConstants.zLengthHalf
        self.chestCenterPoint = self.currentCenterPoint.copy()
        self.chestCenterPoint.z += PersonConstants.zLength34
        self.headCenterPoint = self.currentCenterPoint.copy()
        self.headCenterPoint.z += PersonConstants.zChestLength + (PersonConstants.headSizeHalf)
        self.currentFootRect = self.nextFootRect.copy()

    def addHealth(self, health):
        if health < 0:
            raise Exception("health cannot be negative.")

        self.health = int(Math.min(self.health + health, PersonConstants.maxPersonHealth))

    def damage(self, value):
        if value < 0:
            raise Exception("value cannot be negative.")

        self.health = int(Math.max(self.health - value, 0))

    def isParalyzed(self):
        return not self.paralyzeDelay.isExpired()

    def getModelMatrix(self):
        return (
            TransformMatrix4Builder()
            .translate(self.currentCenterPoint.x, self.currentCenterPoint.y, self.currentCenterPoint.z)
            .rotate(self.yawRadians, CommonConstants.zAxis)
            .resultMatrix
        )
