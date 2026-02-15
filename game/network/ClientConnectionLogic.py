from game.network.EmptyMessageChannel import EmptyMessageChannel
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
        if connectionResult is not None:
            netClient.id = connectionResult.playerId
            netClient.gameState.player.id = connectionResult.playerId
            netClient.channelToServer = NetMessageChannel(connectionResult.portForSendingToServer, connectionResult.portForReceivingFromServer)
            netClient.channelToServer.open()

    def disconnectByNet(self, netClient):
        netClient.channelToServer.close()
        netClient.channelToServer = EmptyMessageChannel.instance
        netClient.id = 0
        netClient.gameState.player.id = 0
