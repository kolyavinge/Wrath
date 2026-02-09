from game.network.MessageSerializer import MessageSerializer


class NetMessageChannel:

    def __init__(self):
        self.messageSerializer = MessageSerializer()

    def sendMessageToClient(self, message):
        pass

    def receiveMessageFromClientOrNone(self):
        pass

    def sendMessageToServer(self, message):
        pass

    def receiveMessageFromServerOrNone(self):
        pass
