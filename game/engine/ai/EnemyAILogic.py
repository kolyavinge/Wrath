from game.engine.ai.StateHandlerCollection import StateHandlerCollection
from game.engine.GameData import GameData


class EnemyAILogic:

    def __init__(self, gameData, stateHandlerCollection):
        self.gameData = gameData
        self.stateHandlerCollection = stateHandlerCollection

    def apply(self):
        for enemy in self.gameData.enemies:
            inputData = self.gameData.enemyInputData[enemy]
            inputData.clear()
            aiData = enemy.aiData
            state = self.stateHandlerCollection.getStateHandler(aiData.state)
            state.process(enemy, inputData)
            newState = state.getNewStateOrNone(enemy)
            if newState is not None:
                aiData.state = newState


def makeEnemyAILogic(resolver):
    return EnemyAILogic(resolver.resolve(GameData), resolver.resolve(StateHandlerCollection))
