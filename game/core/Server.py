from game.model.snapshot.ServerSnapshot import ServerSnapshot


class ConnectedClient:

    def __init__(self):
        self.id = 0
        self.channelToClient = None
        self.lastAcknowledgedServerSnapshot = ServerSnapshot.makeEmpty()


class Server:

    def __init__(self):
        self.gameState = None
        self.clients = {}
