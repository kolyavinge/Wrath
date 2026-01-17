from game.network.LocalMessageChannel import LocalMessageChannel
from game.network.NetMessageChannel import NetMessageChannel


class ServerConnector:

    def connectByLocal(self, localClient, server):
        localClient.id = 1
        localClient.messageChannel = LocalMessageChannel()
        server.clients[localClient.id] = localClient

    def connectByNet(self):
        return NetMessageChannel()

    def disconnect(self, client, server):
        client.id = 0
        client.messageChannel = None
        server.clients.remove(client.id)
