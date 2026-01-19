from game.anx.DebugSettings import DebugSettings
from game.engine.ai.state.StateHandlerCollection import StateHandlerCollection
from game.model.person.PersonStates import LifeCycle
from game.tools.CpuProfiler import cpuProfile


class EnemyAIUpdater:

    def __init__(
        self,
        stateHandlerCollection: StateHandlerCollection,
    ):
        self.stateHandlerCollection = stateHandlerCollection
        if DebugSettings.enemyFreeze:
            self.update = lambda gs: None

    def init(self, gameState):
        for enemy in gameState.enemies:
            self.stateHandlerCollection.getStateHandler(enemy.aiData.state).init(gameState, enemy)

    # @cpuProfile
    def update(self, gameState):
        for enemy, enemyItems in gameState.enemyItems.items():
            inputData = gameState.enemyInputData[enemy]
            inputData.clear()
            if enemy.lifeCycle != LifeCycle.alive or enemy.isParalyzed():
                return
            aiData = enemy.aiData
            stateHandler = self.stateHandlerCollection.getStateHandler(aiData.state)
            stateHandler.process(gameState, enemy, inputData)
            aiData.stateTime += 1
            newState = stateHandler.getNewStateOrNone(gameState, enemy, enemyItems)
            if newState is not None:
                aiData.state = newState
                aiData.stateTime = 0
                self.stateHandlerCollection.getStateHandler(newState).init(gameState, enemy)
