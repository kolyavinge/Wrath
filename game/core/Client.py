from game.model.snapshot.ClientSnapshot import ClientSnapshot


class Client:

    def __init__(self):
        self.id = 0
        self.gameState = None
        self.channelToServer = None
        self.lastAcknowledgedClientSnapshot = ClientSnapshot.makeEmpty()
