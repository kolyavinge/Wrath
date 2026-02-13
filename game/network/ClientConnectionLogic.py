from game.network.GameServiceClient import GameServiceClient
from game.network.LocalMessageChannel import LocalMessageChannel
from game.network.NetMessageChannel import NetMessageChannel


class ClientConnectionLogic:

    def __init__(
        self,
        gameServiceClient: GameServiceClient,
    ):
        self.gameServiceClient = gameServiceClient

    def connectByLocal(self, localClient, server):
        localClient.id = 1
        localClient.messageChannel = LocalMessageChannel()
        server.clients[localClient.id] = localClient

    def connectByNet(self, netClient):
        connectionResult = self.gameServiceClient.connectToServer()
        netClient.id = connectionResult.clientId
        netClient.messageChannel = NetMessageChannel()
        netClient.gameState.player.id = connectionResult.playerId

    def disconnectByLocal(self, localClient, server):
        localClient.id = 0
        localClient.messageChannel = None
        server.clients.remove(localClient.id)

    def disconnectByNet(self, netClient):
        pass
