from game.lib.Math import Math
from game.model.person.Person import Person


class EnemyState:

    patrolling = 1
    fireing = 2


class AIData:

    def __init__(self):
        self.state = EnemyState.patrolling
        self.horizontalFieldViewRadians = 0
        self.checkCollisionLength = 0
        self.checkCollisionDirectionsCount = 0
        self.lengthForFire = 0
        self.targetPerson = None

    def commit(self):
        self.checkCollisionRadianStep = self.horizontalFieldViewRadians / self.checkCollisionDirectionsCount
        self.horizontalFieldViewRadiansHalf = self.horizontalFieldViewRadians / 2.0
        self.horizontalFieldViewHalfCos = Math.cos(self.horizontalFieldViewRadiansHalf)


class Enemy(Person):

    def __init__(self):
        super().__init__()
        self.currentCenterPointLevelSegment = None
        self.aiData = AIData()
