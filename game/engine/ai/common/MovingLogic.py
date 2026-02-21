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

    def orientToFreeDirection(self, bot, collisionTree):
        nextFrontNormal = self.obstacleAvoidanceLogic.getFrontNormalForNextStep(bot, collisionTree)
        if nextFrontNormal.isZero():
            nextFrontNormal = bot.frontNormal.copy()
            nextFrontNormal.mul(-1)
        if not bot.frontNormal.isParallel(nextFrontNormal):
            self.personTurnLogic.orientToFrontNormal(bot, nextFrontNormal)

    def followByRoute(self, bot):
        route = bot.aiData.route
        routePoint = route.getCurrentPoint()
        direction = bot.currentCenterPoint.getDirectionTo(routePoint)
        directionLength = direction.getLength()
        if directionLength > 1.0:
            direction.div(directionLength)  # normalize
            if not bot.frontNormal.isParallel(direction):
                self.personTurnLogic.orientToFrontNormal(bot, direction)
        else:
            route.removeCurrentPoint()

    def updateMoveDirection(self, bot):
        aiData = bot.aiData
        aiData.moveDirectionRemain.decrease()
        if aiData.moveDirectionRemain.isExpired():
            aiData.moveDirection = Random.getListItem(MoveDirections.all)
            aiData.moveDirectionRemain.set(Random.getInt(50, 200))
            aiData.runAwayFromObstacle = False

    def setOppositeMoveDirection(self, bot):
        aiData = bot.aiData
        aiData.moveDirection = aiData.moveDirection.opposite
        aiData.moveDirectionRemain.set(Random.getInt(50, 200))

    def isTurnTimeLimited(self, bot):
        bot.aiData.turnTimeLimit.decrease()
        return bot.aiData.turnTimeLimit.isExpired()

    def applyMoveDirectionInputData(self, bot, inputData):
        bot.aiData.moveDirection.applyInputData(inputData)
