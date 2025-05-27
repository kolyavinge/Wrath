from game.engine.ai.common.ObstacleAvoidanceLogic import ObstacleAvoidanceLogic
from game.engine.person.PersonTurnLogic import PersonTurnLogic
from game.lib.Random import Random
from game.model.ai.MoveDirections import MoveDirections


class MovingLogic:

    def __init__(
        self,
        personTurnLogic: PersonTurnLogic,
        obstacleAvoidanceLogic: ObstacleAvoidanceLogic,
    ):
        self.personTurnLogic = personTurnLogic
        self.obstacleAvoidanceLogic = obstacleAvoidanceLogic

    def orientToFreeDirection(self, enemy):
        nextFrontNormal = self.obstacleAvoidanceLogic.getFrontNormalForNextStep(enemy)
        if nextFrontNormal.isZero():
            nextFrontNormal = enemy.frontNormal.copy()
            nextFrontNormal.mul(-1)
        if not enemy.frontNormal.isParallel(nextFrontNormal):
            self.personTurnLogic.orientToFrontNormal(enemy, nextFrontNormal)

    def followByRoute(self, enemy):
        route = enemy.aiData.route
        routePoint = route.getCurrentPoint()
        direction = enemy.currentCenterPoint.getDirectionTo(routePoint)
        directionLength = direction.getLength()
        if directionLength > 1.0:
            direction.div(directionLength)  # normalize
            if not enemy.frontNormal.isParallel(direction):
                self.personTurnLogic.orientToFrontNormal(enemy, direction)
        else:
            route.removeCurrentPoint()

    def updateMoveDirection(self, enemy):
        aiData = enemy.aiData
        aiData.moveDirectionRemain.decrease()
        if aiData.moveDirectionRemain.isExpired():
            aiData.moveDirection = Random.getListItem(MoveDirections.all)
            aiData.moveDirectionRemain.set(Random.getInt(50, 200))
            aiData.runAwayFromObstacle = False

    def setOppositeMoveDirection(self, enemy):
        aiData = enemy.aiData
        aiData.moveDirection = aiData.moveDirection.opposite
        aiData.moveDirectionRemain.set(Random.getInt(50, 200))

    def isTurnTimeLimited(self, enemy):
        enemy.aiData.turnTimeLimit.decrease()
        return enemy.aiData.turnTimeLimit.isExpired()

    def applyMoveDirectionInputData(self, enemy, inputData):
        enemy.aiData.moveDirection.applyInputData(inputData)
