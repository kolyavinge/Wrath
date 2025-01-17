from game.engine.GameData import GameData


class EnemyAILogic:

    def __init__(self, gameData):
        self.gameData = gameData

    def apply(self):
        for enemy in self.gameData.enemies:
            inputData = self.gameData.enemyInputData[enemy]
            self.applyForEnemy(enemy, inputData)

    def applyForEnemy(self, enemy, inputData):
        # inputData.goForward = True
        pass


def makeEnemyAILogic(resolver):
    return EnemyAILogic(resolver.resolve(GameData))
