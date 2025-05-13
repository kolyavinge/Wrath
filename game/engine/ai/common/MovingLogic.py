from game.engine.ai.common.ObstacleAvoidanceLogic import ObstacleAvoidanceLogic
from game.engine.person.PersonTurnLogic import PersonTurnLogic
from game.lib.Random import Random
from game.model.person.Enemy import MoveDirections


class MovingLogic:

    def __init__(self, personTurnLogic, obstacleAvoidanceLogic):
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
            aiData.moveDirection = self.rand.getInt(0, MoveDirections.count)
            aiData.moveDirectionRemain = self.rand.getInt(0, 100)

    def applyInputData(self, enemy, inputData):
        moveDirection = enemy.aiData.moveDirection
        if moveDirection == MoveDirections.idle:
            return
        elif moveDirection == MoveDirections.forward:
            inputData.goForward = True
        elif moveDirection == MoveDirections.backward:
            inputData.goBackward = True
        elif moveDirection == MoveDirections.left:
            inputData.stepLeft = True
        elif moveDirection == MoveDirections.right:
            inputData.stepRight = True
        elif moveDirection == MoveDirections.forwardLeft:
            inputData.goForward = True
            inputData.stepLeft = True
        elif moveDirection == MoveDirections.forwardRight:
            inputData.goForward = True
            inputData.stepRight = True
        elif moveDirection == MoveDirections.backwardLeft:
            inputData.goBackward = True
            inputData.stepLeft = True
        elif moveDirection == MoveDirections.backwardRight:
            inputData.goBackward = True
            inputData.stepRight = True
        else:
            assert "Wrong MoveDirection"


def makeMovingLogic(resolver):
    return MovingLogic(resolver.resolve(PersonTurnLogic), resolver.resolve(ObstacleAvoidanceLogic))
