from game.network.GameServiceClient import GameServiceClient
from game.network.NetMessageChannel import NetMessageChannel
from game.network.ServerConnector import ServerConnector


# client connection logic
class NetworkConnectionInitializer:

    def __init__(
        self,
        serverConnector: ServerConnector,
        gameServiceClient: GameServiceClient,
    ):
        self.serverConnector = serverConnector
        self.gameServiceClient = gameServiceClient

    def connectByLocal(self, localClient, server):
        self.serverConnector.connectByLocal(localClient, server)

    def connectByNet(self, netClient):
        connectionResult = self.gameServiceClient.connectToServer()
        netClient.id = 0
        netClient.messageChannel = NetMessageChannel()
        netClient.gameState.player.id = self.personIdLogic.getNetPlayerId()
