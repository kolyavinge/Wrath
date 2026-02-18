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
        if connectionResult is None:
            raise Exception("Unable to connect to server.")

        netClient.playerId = connectionResult.playerId
        netClient.channelToServer = NetMessageChannel(connectionResult.portForSendingToServer, connectionResult.portForReceivingFromServer)
        netClient.channelToServer.open()

        return connectionResult.playerId

    def disconnectByNet(self, netClient):
        netClient.channelToServer.close()
        netClient.channelToServer = EmptyMessageChannel.instance
        netClient.playerId = 0
        netClient.gameState.player.id = 0
