from game.anx.CommonConstants import CommonConstants
from game.lib.Time import Time
from game.model.snapshot.ServerSnapshot import ServerSnapshot
from game.multiplayer.EmptyMessageChannel import EmptyMessageChannel


class ConnectedClient:

    def __init__(self):
        self.playerId = 0
        self.ipAddress = ""
        self.channelToClient = EmptyMessageChannel.instance
        self.init()

    def init(self):
        self.lastAcknowledgedServerSnapshot = ServerSnapshot.makeEmpty()
        self.lastAcknowledgedSnapshotTime = Time.getCurrentTimeSec() + CommonConstants.disconnectTimelimitSec


class Server:

    def __init__(self):
        self.gameState = None
        self.clients = {}
        self.disconnectedClientIds = []
