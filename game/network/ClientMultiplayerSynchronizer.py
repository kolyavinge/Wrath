from game.network.GameStateSynchronizer import GameStateSynchronizer
from game.network.Message import Message, MessageType
from game.network.SendMessageResult import SendMessageResult
from game.network.SnapshotDiffLogic import SnapshotDiffLogic
from game.network.SnapshotFactory import SnapshotFactory


class ClientMultiplayerSynchronizer:

    def __init__(
        self,
        snapshotFactory: SnapshotFactory,
        snapshotDiffLogic: SnapshotDiffLogic,
        gameStateSynchronizer: GameStateSynchronizer,
    ):
        self.snapshotFactory = snapshotFactory
        self.snapshotDiffLogic = snapshotDiffLogic
        self.gameStateSynchronizer = gameStateSynchronizer

    def init(self, client):
        self.client = client

    def receiveGameStateFromServer(self):
        message = self.client.channelToServer.receiveMessageOrNone()
        if message is not None:
            assert message.type == MessageType.updateGameState
            diff = message.body
            self.gameStateSynchronizer.applySnapshotDiff(self.client.gameState, diff)

    def sendGameStateToServer(self):
        newSnapshot = self.snapshotFactory.makeClientSnapshot(self.client.gameState)
        diff = self.snapshotDiffLogic.getSnapshotsDiff(self.client.lastAcknowledgedClientSnapshot, newSnapshot)
        if not diff.isEmpty():
            print(f"Client id: {self.client.id} is sending diff to server")
            message = Message(MessageType.updateGameState, diff)
            if self.client.channelToServer.sendMessage(message) == SendMessageResult.sended:
                assert newSnapshot.id > self.client.lastAcknowledgedClientSnapshot.id
                self.client.lastAcknowledgedClientSnapshot = newSnapshot
