from game.engine.ai.FireLogic import FireLogic
from game.engine.ai.MovingLogic import MovingLogic
from game.engine.GameData import GameData


class EnemyAILogic:

    def __init__(self, gameData, movingLogic, fireLogic):
        self.gameData = gameData
        self.movingLogic = movingLogic
        self.fireLogic = fireLogic

    def apply(self):
        for enemy in self.gameData.enemies:
            inputData = self.gameData.enemyInputData[enemy]
            self.applyForEnemy(enemy, inputData)

    def applyForEnemy(self, enemy, inputData):
        inputData.clear()

        if self.fireLogic.targetExists(enemy):
            self.fireLogic.orientToTargetPerson(enemy)
            inputData.fire = self.fireLogic.fire()
        else:
            self.movingLogic.orientToNextDirection(enemy)
            inputData.goForward = True


def makeEnemyAILogic(resolver):
    return EnemyAILogic(resolver.resolve(GameData), resolver.resolve(MovingLogic), resolver.resolve(FireLogic))
