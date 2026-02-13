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
        netClient.id = 0
        netClient.messageChannel = NetMessageChannel()
        netClient.gameState.player.id = self.personIdLogic.getNetPlayerId()
