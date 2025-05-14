from game.engine.ai.common.ObstacleAvoidanceLogic import ObstacleAvoidanceLogic
from game.engine.person.PersonTurnLogic import PersonTurnLogic
from game.lib.Random import Random
from game.model.ai.MoveDirection import MoveDirection


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
            aiData.moveDirection = self.rand.getInt(0, MoveDirection.count)
            aiData.moveDirectionRemain = self.rand.getInt(0, 100)

    def applyInputData(self, enemy, inputData):
        moveDirection = enemy.aiData.moveDirection
        if moveDirection == MoveDirection.idle:
            return
        elif moveDirection == MoveDirection.forward:
            inputData.goForward = True
        elif moveDirection == MoveDirection.backward:
            inputData.goBackward = True
        elif moveDirection == MoveDirection.left:
            inputData.stepLeft = True
        elif moveDirection == MoveDirection.right:
            inputData.stepRight = True
        elif moveDirection == MoveDirection.forwardLeft:
            inputData.goForward = True
            inputData.stepLeft = True
        elif moveDirection == MoveDirection.forwardRight:
            inputData.goForward = True
            inputData.stepRight = True
        elif moveDirection == MoveDirection.backwardLeft:
            inputData.goBackward = True
            inputData.stepLeft = True
        elif moveDirection == MoveDirection.backwardRight:
            inputData.goBackward = True
            inputData.stepRight = True
        else:
            assert "Wrong MoveDirection"
