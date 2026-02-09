from game.model.snapshot.SnapshotDiff import SnapshotDiff


class MessageType:

    connectToServer = 1
    updateGameState = 2


class Message:

    def __init__(self, type):
        if type is None:
            raise Exception("Message type cannot be None.")

        self.type = type
        self.body = None

    def toBytes(self, writer):
        writer.write("b", self.type)
        self.body.toBytes(writer)

    @staticmethod
    def fromBytes(reader):
        message = Message()
        message.type = reader.read("b")
        if message.type == MessageType.connectToServer:
            pass
        elif message.type == MessageType.updateGameState:
            message.body = SnapshotDiff.fromBytes(reader)

        return message
