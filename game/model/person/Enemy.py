from game.lib.Math import Math
from game.model.person.Person import Person


class EnemyState:

    patrolling = 1
    attack = 2
    healthSearch = 3
    weaponSearch = 4


class MoveDirections:

    idle = 0
    forward = 1
    backward = 2
    left = 3
    right = 4
    forwardLeft = 5
    forwardRight = 6
    backwardLeft = 7
    backwardRight = 8
    count = 9


class AIData:

    def __init__(self):
        self.state = EnemyState.patrolling
        self.horizontalFieldViewRadians = 0
        self.checkCollisionLength = 0
        self.checkCollisionDirectionsCount = 0
        self.fireDistance = 0
        self.targetPerson = None
        self.fireBurstRemain = 0
        self.fireDelayRemain = 0
        self.moveDirection = MoveDirections.idle
        self.moveDirectionRemain = 0

    def commit(self):
        self.checkCollisionRadianStep = self.horizontalFieldViewRadians / self.checkCollisionDirectionsCount
        self.horizontalFieldViewRadiansHalf = self.horizontalFieldViewRadians / 2.0
        self.horizontalFieldViewHalfCos = Math.cos(self.horizontalFieldViewRadiansHalf)


class Enemy(Person):

    def __init__(self):
        super().__init__()
        self.currentCenterPointLevelSegment = None
        self.aiData = AIData()
