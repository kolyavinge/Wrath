from game.lib.Math import Math
from game.model.person.Person import Person


class EnemyState:

    patrolling = 1
    attack = 2
    healthSearch = 3
    weaponSearch = 4


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

    def commit(self):
        self.checkCollisionRadianStep = self.horizontalFieldViewRadians / self.checkCollisionDirectionsCount
        self.horizontalFieldViewRadiansHalf = self.horizontalFieldViewRadians / 2.0
        self.horizontalFieldViewHalfCos = Math.cos(self.horizontalFieldViewRadiansHalf)


class Enemy(Person):

    def __init__(self):
        super().__init__()
        self.currentCenterPointLevelSegment = None
        self.aiData = AIData()
