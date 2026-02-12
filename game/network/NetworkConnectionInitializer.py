from game.network.GameServiceClient import GameServiceClient
from game.network.MultiplayerSynchronizer import MultiplayerSynchronizer
from game.network.ServerConnector import ServerConnector


class NetworkConnectionInitializer:

    def __init__(
        self,
        serverConnector: ServerConnector,
        gameServiceClient: GameServiceClient,
        multiplayerSynchronizer: MultiplayerSynchronizer,
    ):
        self.serverConnector = serverConnector
        self.gameServiceClient = gameServiceClient
        self.multiplayerSynchronizer = multiplayerSynchronizer

    def connectByLocal(self, client, server):
        self.serverConnector.connectByLocal(client, server)
        self.multiplayerSynchronizer.init(client, server)

    def connectByNet(self, client):
        connectionResult = self.gameServiceClient.connectToServer()
        self.serverConnector.connectByNet(client)
        self.multiplayerSynchronizer.init(client, None)
