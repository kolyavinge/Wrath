from game.engine.ClientUpdater import ClientUpdater
from game.engine.GameState import GameState
from game.engine.ServerUpdater import ServerUpdater
from game.tools.CpuProfiler import cpuProfile
from game.tools.timeProfile import timeProfile


class GameUpdater:

    def __init__(
        self,
        gameState: GameState,
        clientUpdater: ClientUpdater,
        serverUpdater: ServerUpdater,
    ):
        self.gameState = gameState
        self.clientUpdater = clientUpdater
        self.serverUpdater = serverUpdater

    # @timeProfile("Game updated", CommonConstants.mainTimerMsec / 1000.0, showOnlyLimited=True)
    # @cpuProfile
    def update(self):
        # --- main game loop ---
        self.clientUpdater.update()
        self.serverUpdater.update()
