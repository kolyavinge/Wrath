from game.lib.BinaryReader import BinaryReader
from game.lib.BinaryWriter import BinaryWriter
from game.network.Message import Message


class MessageSerializer:

    def __init__(self):
        self.reader = BinaryReader()
        self.writer = BinaryWriter(Message.maxMessageSizeBytes)

    def toBytes(self, message):
        self.writer.init()
        message.toBytes(self.writer)

        return self.writer.getBytes()

    def fromBytes(self, bytes):
        self.reader.init(bytes)
        message = Message.fromBytes(self.reader)

        return message
