from game.network.SendMessageResult import SendMessageResult


class LocalMessageChannel:

    def __init__(self):
        self.lastClientMessage = None
        self.lastServerMessage = None

    def sendMessageToClient(self, message):
        self.lastServerMessage = message

        return SendMessageResult.sended

    def receiveMessageFromClientOrNone(self):
        result = self.lastClientMessage
        self.lastClientMessage = None

        return result

    def sendMessageToServer(self, message):
        self.lastClientMessage = message

        return SendMessageResult.sended

    def receiveMessageFromServerOrNone(self):
        result = self.lastServerMessage
        self.lastServerMessage = None

        return result
