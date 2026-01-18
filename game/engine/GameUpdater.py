from game.engine.ClientUpdater import ClientUpdater
from game.engine.GameState import GameState
from game.engine.ServerUpdater import ServerUpdater
from game.network.MultiplayerSynchronizer import MultiplayerSynchronizer
from game.tools.CpuProfiler import cpuProfile
from game.tools.timeProfile import timeProfile


class GameUpdater:

    def __init__(
        self,
        gameState: GameState,
        clientUpdater: ClientUpdater,
        serverUpdater: ServerUpdater,
        multiplayerSynchronizer: MultiplayerSynchronizer,
    ):
        self.gameState = gameState
        self.clientUpdater = clientUpdater
        self.serverUpdater = serverUpdater
        self.multiplayerSynchronizer = multiplayerSynchronizer

    # @timeProfile("Game updated", CommonConstants.mainTimerMsec / 1000.0, showOnlyLimited=True)
    # @cpuProfile
    def update(self):
        # --- main game loop ---

        self.multiplayerSynchronizer.receiveGameStateFromServer()
        self.clientUpdater.update(self.gameState)
        self.multiplayerSynchronizer.sendGameStateToServer()

        self.multiplayerSynchronizer.receiveGameStateFromClients()
        self.serverUpdater.update(self.gameState)
        self.multiplayerSynchronizer.sendGameStateToClients()
