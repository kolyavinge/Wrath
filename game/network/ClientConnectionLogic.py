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
        netClient.gameState.player.id = connectionResult.playerId
        netClient.channelToServer = NetMessageChannel(connectionResult.portForSendingToServer, connectionResult.portForReceivingFromServer)
        netClient.channelToServer.open()

    def disconnectByNet(self, netClient):
        netClient.channelToServer.close()
        netClient.channelToServer = None
        netClient.id = 0
        netClient.gameState.player.id = 0
