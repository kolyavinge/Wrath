from game.network.MessageSerializer import MessageSerializer


class NetMessageChannel:

    def __init__(self, portForSending, portForReceiving):
        self.portForSending = portForSending
        self.portForReceiving = portForReceiving
        self.messageSerializer = MessageSerializer()

    def sendMessage(self, message):
        pass

    def receiveMessageOrNone(self):
        pass
