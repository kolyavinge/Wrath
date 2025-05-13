from game.engine.ai.state.StateHandlerCollection import StateHandlerCollection
from game.engine.GameData import GameData


class EnemyAIUpdater:

    def __init__(
        self,
        gameData: GameData,
        stateHandlerCollection: StateHandlerCollection,
    ):
        self.gameData = gameData
        self.stateHandlerCollection = stateHandlerCollection

    def update(self):
        for enemy in self.gameData.enemies:
            inputData = self.gameData.enemyInputData[enemy]
            inputData.clear()
            aiData = enemy.aiData
            state = self.stateHandlerCollection.getStateHandler(aiData.state)
            state.process(enemy, inputData)
            newState = state.getNewStateOrNone(enemy)
            if newState is not None:
                aiData.state = newState
