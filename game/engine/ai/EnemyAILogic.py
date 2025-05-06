from game.engine.ai.StateCollection import StateCollection
from game.engine.GameData import GameData


class EnemyAILogic:

    def __init__(self, gameData, stateCollection):
        self.gameData = gameData
        self.stateCollection = stateCollection

    def apply(self):
        for enemy in self.gameData.enemies:
            inputData = self.gameData.enemyInputData[enemy]
            inputData.clear()
            aiData = enemy.aiData
            state = self.stateCollection.getState(aiData.state)
            state.process(enemy, inputData)
            newState = state.getNewStateOrNone(enemy)
            if newState is not None:
                aiData.state = newState


def makeEnemyAILogic(resolver):
    return EnemyAILogic(resolver.resolve(GameData), resolver.resolve(StateCollection))
