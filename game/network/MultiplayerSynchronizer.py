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

    def init(self, client, server):
        self.client = client
        self.server = server

    def receiveGameStateFromServer(self):
        message = self.client.messageChannel.receiveMessageFromServerOrNone()
        if message is not None:
            assert message.type == MessageType.updateGameState
            diff = message.body
            self.gameStateSynchronizer.applySnapshotDiff(self.client.gameState, diff)

    def sendGameStateToServer(self):
        newSnapshot = self.snapshotFactory.makeClientSnapshot(self.client.gameState)
        diff = self.snapshotDiffLogic.getSnapshotsDiff(self.client.lastAcknowledgedSnapshot, newSnapshot)
        if not diff.isEmpty():
            message = Message(MessageType.updateGameState)
            message.body = diff
            if self.client.messageChannel.sendMessageToServer(message) == SendMessageResult.sended:
                assert newSnapshot.id > self.client.lastAcknowledgedSnapshot.id
                self.client.lastAcknowledgedSnapshot = newSnapshot

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
            diff = self.snapshotDiffLogic.getSnapshotsDiff(client.lastAcknowledgedSnapshot, newSnapshot)
            if not diff.isEmpty():
                message = Message(MessageType.updateGameState)
                message.body = diff
                if client.messageChannel.sendMessageToClient(message) == SendMessageResult.sended:
                    assert newSnapshot.id > self.client.lastAcknowledgedSnapshot.id
                    self.client.lastAcknowledgedSnapshot = newSnapshot
