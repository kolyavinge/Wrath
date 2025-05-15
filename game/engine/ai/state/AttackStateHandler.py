from game.engine.ai.common.FireLogic import FireLogic
from game.engine.ai.common.MovingLogic import MovingLogic
from game.engine.GameData import GameData
from game.model.ai.AIData import EnemyState


class AttackStateHandler:

    def __init__(
        self,
        gameData: GameData,
        movingLogic: MovingLogic,
        fireLogic: FireLogic,
    ):
        self.gameData = gameData
        self.movingLogic = movingLogic
        self.fireLogic = fireLogic

    def process(self, enemy, inputData):
        self.movingLogic.updateMoveDirection(enemy)

        if not enemy.aiData.runAwayFromObstacle and enemy in self.gameData.collisionData.personPerson:
            otherEnemy = self.gameData.collisionData.personPerson[enemy]
            if otherEnemy.velocityValue > 0:
                self.movingLogic.setOppositeOtherEnemyDirection(enemy, otherEnemy.velocityVector)
            else:
                self.movingLogic.setOppositeDirection(enemy)

        self.movingLogic.applyInputData(enemy, inputData)
        self.fireLogic.orientToTargetPerson(enemy)
        self.fireLogic.applyInputData(enemy, inputData)

    def getNewStateOrNone(self, enemy):
        if not self.fireLogic.targetExists(enemy):
            return EnemyState.patrolling

        return None
