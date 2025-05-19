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
        self.rand = Random()

    def orientToNextDirection(self, enemy):
        nextFrontNormal = self.obstacleAvoidanceLogic.getFrontNormalForNextStep(enemy)
        if nextFrontNormal.isZero():
            nextFrontNormal = enemy.frontNormal.copy()
            nextFrontNormal.mul(-1)
        if not enemy.frontNormal.isParallel(nextFrontNormal):
            self.personTurnLogic.orientToFrontNormal(enemy, nextFrontNormal)

    def updateMoveDirection(self, enemy):
        aiData = enemy.aiData
        if aiData.moveDirectionRemain > 0:
            aiData.moveDirectionRemain -= 1
        if aiData.moveDirectionRemain == 0:
            aiData.moveDirection = self.getRandomMoveDirection()
            aiData.moveDirectionRemain = self.rand.getInt(50, 200)
            aiData.runAwayFromObstacle = False

    def setOppositeOtherEnemyDirection(self, enemy, otherEnemy):
        aiData = enemy.aiData
        # otherEnemyOppositeDirection = MoveDirection.fromVector(otherEnemy.velocityVector)
        # aiData.moveDirection = otherEnemyOppositeDirection
        # aiData.moveDirectionRemain = self.rand.getInt(50, 200)

    def setOppositeDirection(self, enemy):
        aiData = enemy.aiData
        aiData.moveDirection = aiData.moveDirection.opposite
        aiData.moveDirectionRemain = self.rand.getInt(50, 200)

    def getRandomMoveDirection(self):
        return MoveDirections.all[self.rand.getInt(0, len(MoveDirections.all) - 1)]

    def applyInputData(self, enemy, inputData):
        enemy.aiData.moveDirection.applyInputData(inputData)
