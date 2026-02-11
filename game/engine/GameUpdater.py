from game.engine.ClientUpdater import ClientUpdater
from game.engine.ServerUpdater import ServerUpdater
from game.network.MultiplayerSynchronizer import MultiplayerSynchronizer
from game.tools.CpuProfiler import cpuProfile
from game.tools.timeProfile import timeProfile


class GameUpdater:

    def __init__(
        self,
        clientUpdater: ClientUpdater,
        serverUpdater: ServerUpdater,
        multiplayerSynchronizer: MultiplayerSynchronizer,
    ):
        self.clientUpdater = clientUpdater
        self.serverUpdater = serverUpdater
        self.multiplayerSynchronizer = multiplayerSynchronizer

    def init(self, clientGameState, serverGameState):
        self.clientGameState = clientGameState
        self.serverGameState = serverGameState

    # @timeProfile("Game updated", CommonConstants.mainTimerMsec / 1000.0, showOnlyLimited=True)
    # @cpuProfile
    def update(self):
        # --- main game loop ---

        self.clientUpdater.clear(self.clientGameState)
        self.multiplayerSynchronizer.receiveGameStateFromServer()
        self.clientUpdater.update(self.clientGameState)
        self.multiplayerSynchronizer.sendGameStateToServer()

        self.serverUpdater.clear(self.serverGameState)
        self.multiplayerSynchronizer.receiveGameStateFromClients()
        self.serverUpdater.update(self.serverGameState)
        self.multiplayerSynchronizer.sendGameStateToClients()
