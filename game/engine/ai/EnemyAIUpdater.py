from game.anx.DebugSettings import DebugSettings
from game.engine.ai.state.StateHandlerCollection import StateHandlerCollection
from game.engine.GameState import GameState
from game.model.person.PersonStates import LifeCycle
from game.tools.CpuProfiler import cpuProfile


class EnemyAIUpdater:

    def __init__(
        self,
        gameData: GameState,
        stateHandlerCollection: StateHandlerCollection,
    ):
        self.gameData = gameData
        self.stateHandlerCollection = stateHandlerCollection
        if DebugSettings.enemyFreeze:
            self.update = lambda: None

    def init(self):
        for enemy in self.gameData.enemies:
            self.stateHandlerCollection.getStateHandler(enemy.aiData.state).init(enemy)

    # @cpuProfile
    def update(self):
        for enemy in self.gameData.enemies:
            inputData = self.gameData.enemyInputData[enemy]
            inputData.clear()
            if enemy.lifeCycle != LifeCycle.alive or enemy.isParalyzed():
                return
            aiData = enemy.aiData
            stateHandler = self.stateHandlerCollection.getStateHandler(aiData.state)
            stateHandler.process(enemy, inputData)
            aiData.stateTime += 1
            newState = stateHandler.getNewStateOrNone(enemy)
            if newState is not None:
                aiData.state = newState
                aiData.stateTime = 0
                self.stateHandlerCollection.getStateHandler(newState).init(enemy)
