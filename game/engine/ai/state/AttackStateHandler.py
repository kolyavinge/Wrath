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

    def init(self, enemy):
        pass

    def process(self, enemy, inputData):
        self.movingLogic.updateMoveDirection(enemy)

        if not enemy.aiData.runAwayFromObstacle and enemy in self.gameData.collisionData.personPerson:
            enemy.aiData.runAwayFromObstacle = True
            otherEnemy = self.gameData.collisionData.personPerson[enemy]
            if enemy.velocityValue > 0 and otherEnemy.velocityValue > 0:
                if not enemy.velocityVector.isParallel(otherEnemy.velocityVector, 0.1):
                    self.movingLogic.setOppositeDirection(enemy)
            else:
                self.movingLogic.setOppositeDirection(enemy)

        self.movingLogic.applyInputData(enemy, inputData)
        self.fireLogic.orientToTargetPerson(enemy)
        self.fireLogic.applyInputData(enemy, inputData)

    def getNewStateOrNone(self, enemy):
        if not self.fireLogic.targetExists(enemy):
            return EnemyState.patrolling

        if enemy.health < enemy.aiData.criticalHealth:
            return EnemyState.healthSearch

        return None
