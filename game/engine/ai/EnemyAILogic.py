from game.engine.ai.ObstacleAvoidanceLogic import ObstacleAvoidanceLogic
from game.engine.GameData import GameData
from game.engine.PersonTurnLogic import PersonTurnLogic
from game.lib.Numeric import Numeric


class EnemyAILogic:

    def __init__(self, gameData, obstacleAvoidanceLogic, personTurnLogic):
        self.gameData = gameData
        self.obstacleAvoidanceLogic = obstacleAvoidanceLogic
        self.personTurnLogic = personTurnLogic

    def apply(self):
        for enemy in self.gameData.enemies:
            inputData = self.gameData.enemyInputData[enemy]
            self.applyForEnemy(enemy, inputData)

    def applyForEnemy(self, enemy, inputData):
        nextFrontNormal = self.obstacleAvoidanceLogic.getFrontNormalForNextStep(enemy)
        if nextFrontNormal.isZero():
            nextFrontNormal = enemy.frontNormal.copy()
            nextFrontNormal.mul(-1)
        if not Numeric.floatEquals(nextFrontNormal.dotProduct(enemy.frontNormal), 1.0, 0.01):
            self.personTurnLogic.orientByFrontNormal(enemy, nextFrontNormal)
        inputData.goForward = True


def makeEnemyAILogic(resolver):
    return EnemyAILogic(resolver.resolve(GameData), resolver.resolve(ObstacleAvoidanceLogic), resolver.resolve(PersonTurnLogic))
