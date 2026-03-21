from socket import AF_INET, SOCK_STREAM, socket

from game.anx.ConfigManager import ConfigManager
from game.multiplayer.contracts import EmptyRequest
from game.multiplayer.Message import Message, MessageType
from game.multiplayer.MessageSerializer import MessageSerializer


class GameServiceClient:

    def __init__(
        self,
        messageSerializer: MessageSerializer,
        configManager: ConfigManager,
    ):
        self.messageSerializer = messageSerializer
        self.serverAddress = configManager.serverAddress
        self.serverPort = configManager.serverPort

    def connectToServer(self):
        requestMessage = Message(MessageType.connectToServerRequest, EmptyRequest())
        responseMessage = self.sendRequest(requestMessage)
        if responseMessage is None:
            return None

        assert responseMessage.type == MessageType.connectToServerResponse
        response = responseMessage.body

        return response

    def sendRequest(self, requestMessage):
        try:
            with socket(AF_INET, SOCK_STREAM) as tcpSender:
                tcpSender.connect((self.serverAddress, self.serverPort))
                messageBytes, messageLength = self.messageSerializer.toBytes(requestMessage)
                tcpSender.sendall(messageBytes[:messageLength])
                messageBytes = tcpSender.recv(Message.maxMessageSizeBytes)
                responseMessage = self.messageSerializer.fromBytes(messageBytes)

                return responseMessage
        except ConnectionRefusedError:
            return None
