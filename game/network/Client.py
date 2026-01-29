from game.model.snapshot.ClientSnapshot import ClientSnapshot
from game.model.snapshot.ServerSnapshot import ServerSnapshot


class Client:

    def __init__(self):
        self.id = 0
        self.gameState = None
        self.messageChannel = None
        self.lastAcknowledgedClientSnapshot = ClientSnapshot.makeEmpty()
        self.lastAcknowledgedServerSnapshot = ServerSnapshot.makeEmpty()
