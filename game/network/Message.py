class MessageType:

    connectToServer = 1
    updateGameState = 2


class Message:

    def __init__(self, type):
        if type is None:
            raise Exception("Message type cannot be None.")

        self.type = type
        self.body = None
