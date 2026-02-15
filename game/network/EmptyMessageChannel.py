class EmptyMessageChannel:

    def open(self):
        pass

    def close(self):
        pass

    def sendMessage(self, message):
        pass

    def receiveMessageOrNone(self):
        pass


EmptyMessageChannel.instance = EmptyMessageChannel()
