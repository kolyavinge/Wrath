from game.anx.DebugSettings import DebugSettings
from game.engine.ai.state.StateHandlerCollection import StateHandlerCollection
from game.model.person.PersonStates import LifeCycle
from game.tools.CpuProfiler import cpuProfile


class BotAIUpdater:

    def __init__(
        self,
        stateHandlerCollection: StateHandlerCollection,
    ):
        self.stateHandlerCollection = stateHandlerCollection
        if DebugSettings.botFreeze:
            self.update = lambda gs: None

    def init(self, gameState):
        for bot in gameState.bots:
            self.stateHandlerCollection.getStateHandler(bot.aiData.state).init(gameState, bot)

    # @cpuProfile
    def update(self, gameState):
        for bot, botItems in gameState.botItems.items():
            inputData = gameState.botInputData[bot]
            inputData.clear()
            if bot.lifeCycle != LifeCycle.alive or bot.isParalyzed():
                return
            aiData = bot.aiData
            stateHandler = self.stateHandlerCollection.getStateHandler(aiData.state)
            stateHandler.process(gameState, bot, inputData)
            aiData.stateTime += 1
            newState = stateHandler.getNewStateOrNone(gameState, bot, botItems)
            if newState is not None:
                aiData.state = newState
                aiData.stateTime = 0
                self.stateHandlerCollection.getStateHandler(newState).init(gameState, bot)
