from game.network.Snapshot import Snapshot


class Client:

    def __init__(self):
        self.id = 0
        self.gameState = None
        self.messageChannel = None
        self.lastAcknowledgedClientSnapshot = Snapshot.empty
        self.lastAcknowledgedServerSnapshot = Snapshot.empty
