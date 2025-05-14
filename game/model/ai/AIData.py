from game.lib.Math import Math
from game.model.ai.EnemyState import EnemyState
from game.model.ai.MoveDirection import MoveDirection


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
        self.moveDirection = MoveDirection.idle
        self.moveDirectionRemain = 0

    def commit(self):
        self.checkCollisionRadianStep = self.horizontalFieldViewRadians / self.checkCollisionDirectionsCount
        self.horizontalFieldViewRadiansHalf = self.horizontalFieldViewRadians / 2.0
        self.horizontalFieldViewHalfCos = Math.cos(self.horizontalFieldViewRadiansHalf)
