from game.model.snapshot.ServerSnapshot import ServerSnapshot
from game.network.EmptyMessageChannel import EmptyMessageChannel


class ConnectedClient:

    def __init__(self):
        self.playerId = 0
        self.ipAddress = ""
        self.channelToClient = EmptyMessageChannel.instance
        self.lastAcknowledgedServerSnapshot = ServerSnapshot.makeEmpty()

    def resetLastSnapshot(self):
        self.lastAcknowledgedServerSnapshot = ServerSnapshot.makeEmpty()


class Server:

    def __init__(self):
        self.gameState = None
        self.clients = {}
