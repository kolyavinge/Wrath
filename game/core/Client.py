from game.model.snapshot.ClientSnapshot import ClientSnapshot
from game.network.EmptyMessageChannel import EmptyMessageChannel


class Client:

    def __init__(self):
        self.id = 0
        self.gameState = None
        self.channelToServer = EmptyMessageChannel.instance
        self.lastAcknowledgedClientSnapshot = ClientSnapshot.makeEmpty()
