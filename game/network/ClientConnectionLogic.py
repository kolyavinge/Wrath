from game.network.GameServiceClient import GameServiceClient
from game.network.NetMessageChannel import NetMessageChannel


class ClientConnectionLogic:

    def __init__(
        self,
        gameServiceClient: GameServiceClient,
    ):
        self.gameServiceClient = gameServiceClient

    def connectByNet(self, netClient):
        connectionResult = self.gameServiceClient.connectToServer()
        netClient.id = connectionResult.playerId
        netClient.channelToServer = NetMessageChannel(connectionResult.portForSendingToServer, connectionResult.portForReceivingFromServer)
        netClient.gameState.player.id = connectionResult.playerId

    def disconnectByNet(self, netClient):
        netClient.id = 0
        netClient.channelToServer = None
        netClient.gameState.player.id = 0
