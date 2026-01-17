from game.network.MultiplayerSynchronizer import MultiplayerSynchronizer
from game.network.ServerConnector import ServerConnector


class NetworkConnectionInitializer:

    def __init__(
        self,
        serverConnector: ServerConnector,
        multiplayerSynchronizer: MultiplayerSynchronizer,
    ):
        self.serverConnector = serverConnector
        self.multiplayerSynchronizer = multiplayerSynchronizer

    def init(self, client, server):
        self.serverConnector.connectByLocal(client, server)
        self.multiplayerSynchronizer.init(client, server)
