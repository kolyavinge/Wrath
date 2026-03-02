from game.anx.CommonConstants import CommonConstants
from game.lib.Time import Time
from game.network.GameStateSynchronizer import GameStateSynchronizer
from game.network.Message import Message, MessageType
from game.network.SendMessageResult import SendMessageResult
from game.network.ServerConnectionLogic import ServerConnectionLogic
from game.network.SnapshotDiffLogic import SnapshotDiffLogic
from game.network.SnapshotFactory import SnapshotFactory


class ServerMultiplayerSynchronizer:

    def __init__(
        self,
        snapshotFactory: SnapshotFactory,
        snapshotDiffLogic: SnapshotDiffLogic,
        gameStateSynchronizer: GameStateSynchronizer,
        serverConnectionLogic: ServerConnectionLogic,
    ):
        self.snapshotFactory = snapshotFactory
        self.snapshotDiffLogic = snapshotDiffLogic
        self.gameStateSynchronizer = gameStateSynchronizer
        self.serverConnectionLogic = serverConnectionLogic

    def init(self, server):
        self.server = server

    def receiveGameStateFromClients(self):
        for client in self.server.clients.values():
            message = client.channelToClient.receiveMessageOrNone()
            if message is not None:
                assert message.type == MessageType.updateGameState
                diff = message.body
                self.gameStateSynchronizer.applySnapshotDiff(self.server.gameState, diff)

    def sendGameStateToClients(self):
        newSnapshot = self.snapshotFactory.makeServerSnapshot(self.server.gameState)
        for client in self.server.clients.values():
            diff = self.snapshotDiffLogic.getSnapshotsDiff(client.lastAcknowledgedServerSnapshot, newSnapshot, client.playerId)
            if not diff.isEmpty():
                message = Message(MessageType.updateGameState, diff)
                if client.channelToClient.sendMessage(message) == SendMessageResult.sended:
                    assert newSnapshot.id > client.lastAcknowledgedServerSnapshot.id
                    client.lastAcknowledgedServerSnapshot = newSnapshot
                    client.lastAcknowledgedSnapshotTime = Time.getCurrentTimeSec()
                else:
                    if Time.getCurrentTimeSec() - client.lastAcknowledgedSnapshotTime > CommonConstants.disconnectTimelimitSec:
                        self.server.disconnectedClientIds.append(client.playerId)
                        self.serverConnectionLogic.disconnectByNet(client)

        if len(self.server.disconnectedClientIds) > 0:
            for clientId in self.server.disconnectedClientIds:
                self.server.clients.pop(clientId)
            self.server.disconnectedClientIds = []
