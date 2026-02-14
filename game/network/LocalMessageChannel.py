from game.network.SendMessageResult import SendMessageResult


class MessageHolder:

    def __init__(self):
        self.message = None


class LocalMessageChannel:

    def __init__(self, holderForSending, holderForReceiving):
        self.holderForSending = holderForSending
        self.holderForReceiving = holderForReceiving

    def sendMessage(self, message):
        self.holderForSending.message = message

        return SendMessageResult.sended

    def receiveMessageOrNone(self):
        result = self.holderForReceiving.message
        self.holderForReceiving.message = None

        return result
