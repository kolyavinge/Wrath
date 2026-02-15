from game.lib.TcpService import TcpService
from game.network.contracts import ConnectToServerResponse
from game.network.Message import Message, MessageType
from game.network.MessageSerializer import MessageSerializer
from game.network.ServerConnectionLogic import ServerConnectionLogic


class GameService(TcpService):

    def __init__(
        self,
        messageSerializer: MessageSerializer,
        serverConnectionLogic: ServerConnectionLogic,
    ):
        self.messageSerializer = messageSerializer
        self.serverConnectionLogic = serverConnectionLogic

    def receive(self, clientSocket, clientAddress):
        messageBytes = clientSocket.recv(Message.maxMessageSizeBytes)
        requestMessage = self.messageSerializer.fromBytes(messageBytes)
        responseMessage = self.processMessage(requestMessage)
        messageBytes, messageLength = self.messageSerializer.toBytes(responseMessage)
        clientSocket.sendall(messageBytes[:messageLength])

    def processMessage(self, requestMessage):
        if requestMessage.type == MessageType.connectToServerRequest:
            playerId, portForSendingToServer, portForReceivingFromServer = self.serverConnectionLogic.connectByNet()
            response = ConnectToServerResponse(playerId, portForSendingToServer, portForReceivingFromServer)
            responseMessage = Message(MessageType.connectToServerResponse, response)

            return responseMessage
        else:
            raise Exception("Wrong message type.")

    def onBeginListen(self):
        print("GameService is running")

    def onEndListen(self):
        print("GameService was stopped")
