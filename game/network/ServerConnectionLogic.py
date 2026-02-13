from game.anx.PersonIdLogic import PersonIdLogic
from game.core.Client import Client
from game.network.LocalMessageChannel import LocalMessageChannel
from game.network.NetMessageChannel import NetMessageChannel


class ServerConnectionLogic:

    def __init__(self, personIdLogic: PersonIdLogic):
        self.personIdLogic = personIdLogic

    def connect(self, netClient, server):
        netClient.id = 0
        netClient.messageChannel = NetMessageChannel()
        netClient.gameState.player.id = self.personIdLogic.getNetPlayerId()
        server.clients[netClient.id] = netClient

        return (netClient.id, netClient.gameState.player.id)

    def disconnect(self, netClient, server):
        netClient.id = 0
        netClient.messageChannel = None
        server.clients.remove(netClient.id)
