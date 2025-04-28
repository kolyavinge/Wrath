from game.engine.ai.ObstacleAvoidanceLogic import ObstacleAvoidanceLogic
from game.engine.GameData import GameData
from game.engine.PersonTurnLogic import PersonTurnLogic


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
        frontNormal = self.obstacleAvoidanceLogic.getFrontNormalForNextStep(enemy)
        assert not frontNormal.isZero()
        self.personTurnLogic.orientByFrontNormal(enemy, frontNormal)
        inputData.goForward = True


def makeEnemyAILogic(resolver):
    return EnemyAILogic(resolver.resolve(GameData), resolver.resolve(ObstacleAvoidanceLogic), resolver.resolve(PersonTurnLogic))
