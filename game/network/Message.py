from game.model.snapshot.SnapshotDiff import SnapshotDiff
from game.network.contracts import *


class MessageType:

    connectToServerRequest = 1
    connectToServerResponse = 2
    updateGameState = 3


class Message:

    maxMessageSizeBytes = 4 * 1024

    def __init__(self, type, body):
        self.type = type
        self.body = body

    def toBytes(self, writer):
        writer.write("b", self.type)
        self.body.toBytes(writer)

    @staticmethod
    def fromBytes(reader):
        type = reader.read("b")
        if type == MessageType.connectToServerRequest:
            body = EmptyRequest.fromBytes(reader)
        elif type == MessageType.connectToServerResponse:
            body = ConnectToServerResponse.fromBytes(reader)
        elif type == MessageType.updateGameState:
            body = SnapshotDiff.fromBytes(reader)

        return Message(type, body)
