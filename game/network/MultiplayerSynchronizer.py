# Quake III client-server architecture
# https://fabiensanglard.net/quake3/network.php


from game.network.GameStateSynchronizer import GameStateSynchronizer
from game.network.Message import Message, MessageType
from game.network.SendMessageResult import SendMessageResult
from game.network.SnapshotDiffLogic import SnapshotDiffLogic
from game.network.SnapshotFactory import SnapshotFactory


class MultiplayerSynchronizer:

    def __init__(
        self,
        snapshotFactory: SnapshotFactory,
        snapshotDiffLogic: SnapshotDiffLogic,
        gameStateSynchronizer: GameStateSynchronizer,
    ):
        self.snapshotFactory = snapshotFactory
        self.snapshotDiffLogic = snapshotDiffLogic
        self.gameStateSynchronizer = gameStateSynchronizer

    def init(self, server):
        self.server = server

    def receiveGameStateFromClients(self):
        for client in self.server.clients.values():
            message = client.messageChannel.receiveMessageFromClientOrNone()
            if message is not None:
                assert message.type == MessageType.updateGameState
                diff = message.body
                self.gameStateSynchronizer.applySnapshotDiff(self.server.gameState, diff)

    def sendGameStateToClients(self):
        newSnapshot = self.snapshotFactory.makeServerSnapshot(self.server.gameState)
        for client in self.server.clients.values():
            diff = self.snapshotDiffLogic.getSnapshotsDiff(client.lastAcknowledgedServerSnapshot, newSnapshot)
            if not diff.isEmpty():
                message = Message(MessageType.updateGameState, diff)
                if client.messageChannel.sendMessageToClient(message) == SendMessageResult.sended:
                    assert newSnapshot.id > client.lastAcknowledgedServerSnapshot.id
                    client.lastAcknowledgedServerSnapshot = newSnapshot
