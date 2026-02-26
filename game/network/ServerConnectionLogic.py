from game.anx.CommonConstants import CommonConstants
from game.anx.ConfigManager import ConfigManager
from game.anx.PersonIdLogic import PersonIdLogic
from game.core.Server import ConnectedClient
from game.engine.person.PersonInitializer import PersonInitializer
from game.lib.NetPortManager import NetPortManager
from game.network.EmptyMessageChannel import EmptyMessageChannel
from game.network.LocalMessageChannel import LocalMessageChannel, MessageHolder
from game.network.NetMessageChannel import NetMessageChannel


class ServerConnectionLogic:

    def __init__(
        self,
        personInitializer: PersonInitializer,
        personIdLogic: PersonIdLogic,
        netPortManager: NetPortManager,
        configManager: ConfigManager,
    ):
        self.personInitializer = personInitializer
        self.personIdLogic = personIdLogic
        self.netPortManager = netPortManager
        self.serverAddress = configManager.serverAddress

    def init(self, server):
        self.server = server

    def connectByLocal(self, localClient):
        playerId = self.personIdLogic.getPlayerId()
        clientHolder = MessageHolder()
        serverHolder = MessageHolder()
        localClient.playerId = playerId
        localClient.channelToServer = LocalMessageChannel(clientHolder, serverHolder)
        connectedLocalClient = ConnectedClient()
        connectedLocalClient.playerId = playerId
        connectedLocalClient.channelToClient = LocalMessageChannel(serverHolder, clientHolder)
        self.server.clients[localClient.playerId] = connectedLocalClient
        self.personInitializer.addPlayerToServer(self.server.gameState, localClient.playerId)

        return playerId

    def connectByNet(self, clientAddressAndPort):
        if len(self.server.clients) == CommonConstants.maxServerPlayers:
            raise Exception("Max server players has exceeded.")

        clientAddress, _ = clientAddressAndPort
        playerId = self.personIdLogic.getNetPlayerId()
        portForSendingToServer = self.netPortManager.getFreePort()
        portForReceivingFromServer = self.netPortManager.getFreePort()
        connectedNetClient = ConnectedClient()
        connectedNetClient.playerId = playerId
        connectedNetClient.channelToClient = NetMessageChannel(clientAddress, portForReceivingFromServer, self.serverAddress, portForSendingToServer)
        self.server.clients[connectedNetClient.playerId] = connectedNetClient
        self.personInitializer.addPlayerToServer(self.server.gameState, connectedNetClient.playerId)
        connectedNetClient.channelToClient.open()

        return (playerId, portForSendingToServer, portForReceivingFromServer)

    def disconnectByNet(self, netClient):
        self.server.clients.remove(netClient.playerId)
        netClient.channelToServer.close()
        netClient.channelToServer = EmptyMessageChannel.instance
        netClient.playerId = 0
