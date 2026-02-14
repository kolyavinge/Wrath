class EmptyRequest:

    def toBytes(self, writer):
        pass

    @staticmethod
    def fromBytes(reader):
        return EmptyRequest()


class ConnectToServerResponse:

    def __init__(self, playerId, portForSendingToServer, portForReceivingFromServer):
        self.playerId = playerId
        self.portForSendingToServer = portForSendingToServer
        self.portForReceivingFromServer = portForReceivingFromServer

    def toBytes(self, writer):
        writer.write("iii", self.playerId, self.portForSendingToServer, self.portForReceivingFromServer)

    @staticmethod
    def fromBytes(reader):
        playerId, portForSendingToServer, portForReceivingFromServer = reader.read("iii")
        response = ConnectToServerResponse(playerId, portForSendingToServer, portForReceivingFromServer)

        return response
