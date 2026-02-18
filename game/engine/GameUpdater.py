from game.anx.CommonConstants import CommonConstants
from game.engine.ClientUpdater import ClientUpdater
from game.engine.ServerUpdater import ServerUpdater
from game.network.ClientMultiplayerSynchronizer import ClientMultiplayerSynchronizer
from game.network.ServerMultiplayerSynchronizer import ServerMultiplayerSynchronizer
from game.tools.CpuProfiler import cpuProfile
from game.tools.timeProfile import timeProfile


class GameUpdater:

    def __init__(
        self,
        clientUpdater: ClientUpdater,
        serverUpdater: ServerUpdater,
        clientMultiplayerSynchronizer: ClientMultiplayerSynchronizer,
        serverMultiplayerSynchronizer: ServerMultiplayerSynchronizer,
    ):
        self.clientUpdater = clientUpdater
        self.serverUpdater = serverUpdater
        self.clientMultiplayerSynchronizer = clientMultiplayerSynchronizer
        self.serverMultiplayerSynchronizer = serverMultiplayerSynchronizer
        self.clientGameState = None
        self.serverGameState = None

    def initForClientServer(self, clientGameState, serverGameState):
        self.clientGameState = clientGameState
        self.serverGameState = serverGameState
        self.update = self.updateClientServer

    def initForClient(self, clientGameState):
        self.clientGameState = clientGameState
        self.update = self.updateClient

    # --- main game loop ---
    def update(self):
        pass

    # @timeProfile("Game updated", CommonConstants.mainTimerMsec / 1000.0, showOnlyLimited=False)
    # @cpuProfile
    def updateClientServer(self):
        self.clientUpdater.clear(self.clientGameState)
        self.clientMultiplayerSynchronizer.receiveGameStateFromServer()
        self.clientUpdater.update(self.clientGameState)
        self.clientMultiplayerSynchronizer.sendGameStateToServer()

        self.serverUpdater.clear(self.serverGameState)
        self.serverMultiplayerSynchronizer.receiveGameStateFromClients()
        self.serverUpdater.update(self.serverGameState)
        self.serverMultiplayerSynchronizer.sendGameStateToClients()

    # @timeProfile("Game updated", CommonConstants.mainTimerMsec / 1000.0, showOnlyLimited=False)
    # @cpuProfile
    def updateClient(self):
        self.clientUpdater.clear(self.clientGameState)
        self.clientMultiplayerSynchronizer.receiveGameStateFromServer()
        self.clientUpdater.update(self.clientGameState)
        self.clientMultiplayerSynchronizer.sendGameStateToServer()
