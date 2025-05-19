from game.lib.Math import Math
from game.model.ai.EnemyState import EnemyState
from game.model.ai.MoveDirections import MoveDirections


class AIData:

    def __init__(self):
        self.state = EnemyState.patrolling
        self.stateTime = 0
        self.horizontalFieldViewRadians = 0
        self.checkCollisionLength = 0
        self.checkCollisionDirectionsCount = 0
        self.fireDistance = 0
        self.targetPerson = None
        self.fireBurstRemain = 0
        self.fireDelayRemain = 0
        self.moveDirection = MoveDirections.stay
        self.moveDirectionRemain = 0
        self.runAwayFromObstacle = False
        self.criticalHealth = 0
        self.idleTimeLimit = 0
        self.patrollingTimeLimit = 0
        self.idleTurnTimeLimit = 0

    def commit(self):
        self.checkCollisionRadianStep = self.horizontalFieldViewRadians / self.checkCollisionDirectionsCount
        self.horizontalFieldViewRadiansHalf = self.horizontalFieldViewRadians / 2.0
        self.horizontalFieldViewHalfCos = Math.cos(self.horizontalFieldViewRadiansHalf)
