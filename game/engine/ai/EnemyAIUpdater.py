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

    def init(self):
        for enemy in self.gameData.enemies:
            self.stateHandlerCollection.getStateHandler(enemy.aiData.state).init(enemy)

    def update(self):
        for enemy in self.gameData.enemies:
            inputData = self.gameData.enemyInputData[enemy]
            inputData.clear()
            aiData = enemy.aiData
            stateHandler = self.stateHandlerCollection.getStateHandler(aiData.state)
            stateHandler.process(enemy, inputData)
            aiData.stateTime += 1
            newState = stateHandler.getNewStateOrNone(enemy)
            if newState is not None:
                aiData.state = newState
                aiData.stateTime = 0
                self.stateHandlerCollection.getStateHandler(newState).init(enemy)
