from game.lib.DecrementCounter import DecrementCounter
from game.lib.Math import Math
from game.model.ai.BotState import BotState
from game.model.ai.MoveDirections import MoveDirections
from game.model.ai.Route import NullRoute


class AIData:

    def __init__(self):
        self.state = BotState.patrolling
        self.stateTime = 0
        self.horizontalFieldViewRadians = 0
        self.checkCollisionLength = 0
        self.checkCollisionDirectionsCount = 0
        self.fireDistance = 0
        self.targetPerson = None
        self.fireBurstRemain = DecrementCounter()
        self.fireDelayRemain = DecrementCounter()
        self.moveDirection = MoveDirections.stay
        self.moveDirectionRemain = DecrementCounter()
        self.route = NullRoute.instance
        self.runAwayFromObstacle = False
        self.criticalHealth = 0
        self.turnTimeLimit = DecrementCounter()
        self.idleTimeLimit = DecrementCounter()
        self.patrollingTimeLimit = DecrementCounter()
        self.healthPowerupDelay = DecrementCounter()
        self.weaponPowerupDelay = DecrementCounter()

    def commit(self):
        self.checkCollisionRadianStep = self.horizontalFieldViewRadians / self.checkCollisionDirectionsCount
        self.horizontalFieldViewRadiansHalf = self.horizontalFieldViewRadians / 2.0
        self.horizontalFieldViewHalfCos = Math.cos(self.horizontalFieldViewRadiansHalf)
