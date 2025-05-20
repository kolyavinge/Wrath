from game.engine.ai.common.FireLogic import FireLogic
from game.engine.ai.common.MovingLogic import MovingLogic
from game.engine.GameData import GameData
from game.lib.Random import Random
from game.model.ai.AIData import EnemyState


class PatrollingStateHandler:

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
        enemy.aiData.patrollingTimeLimit = Random.getInt(500, 2000)

    def process(self, enemy, inputData):
        self.movingLogic.orientToNextDirection(enemy)
        inputData.goForward = True

    def getNewStateOrNone(self, enemy):
        if enemy.aiData.stateTime > enemy.aiData.patrollingTimeLimit:
            return EnemyState.idle

        if enemy.health < enemy.aiData.criticalHealth:
            return EnemyState.healthSearch

        otherEnemy = self.fireLogic.getEnemyWithinFireDistanceWhoFiringTo(enemy)
        if otherEnemy is not None:
            enemy.aiData.targetPerson = otherEnemy
            return EnemyState.attack

        if self.fireLogic.targetExists(enemy):
            return EnemyState.attack

        return None
