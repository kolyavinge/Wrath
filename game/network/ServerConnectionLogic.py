from game.anx.PersonIdLogic import PersonIdLogic
from game.core.Server import ConnectedClient
from game.lib.NetPortManager import NetPortManager
from game.network.LocalMessageChannel import LocalMessageChannel, MessageHolder
from game.network.NetMessageChannel import NetMessageChannel


class ServerConnectionLogic:

    def __init__(
        self,
        personIdLogic: PersonIdLogic,
        netPortManager: NetPortManager,
    ):
        self.personIdLogic = personIdLogic
        self.netPortManager = netPortManager

    def init(self, server):
        self.server = server

    def connectByLocal(self, localClient):
        clientHolder = MessageHolder()
        serverHolder = MessageHolder()
        localClient.id = 1
        localClient.channelToServer = LocalMessageChannel(clientHolder, serverHolder)
        connectedLocalClient = ConnectedClient()
        connectedLocalClient.id = localClient.id
        connectedLocalClient.channelToClient = LocalMessageChannel(serverHolder, clientHolder)
        self.server.clients[localClient.id] = connectedLocalClient

    def connectByNet(self):
        playerId = self.personIdLogic.getNetPlayerId()
        portForSendingToServer = self.netPortManager.getFreePort()
        portForReceivingFromServer = self.netPortManager.getFreePort()
        connectedNetClient = ConnectedClient()
        connectedNetClient.id = playerId
        connectedNetClient.channelToClient = NetMessageChannel(portForReceivingFromServer, portForSendingToServer)
        self.server.clients[connectedNetClient.id] = connectedNetClient

        return (playerId, portForSendingToServer, portForReceivingFromServer)

    def disconnectByNet(self, netClient):
        self.server.clients.remove(netClient.id)
        netClient.messageChannel = None
        netClient.id = 0
