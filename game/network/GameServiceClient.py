from socket import AF_INET, SOCK_STREAM, socket

from game.network.contracts import EmptyRequest
from game.network.Message import Message, MessageType
from game.network.MessageSerializer import MessageSerializer


class GameServiceClient:

    def __init__(
        self,
        messageSerializer: MessageSerializer,
    ):
        self.messageSerializer = messageSerializer

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
                tcpSender.connect(("127.0.0.1", 6464))
                messageBytes, messageLength = self.messageSerializer.toBytes(requestMessage)
                tcpSender.sendall(messageBytes[:messageLength])
                messageBytes = tcpSender.recv(Message.maxMessageSizeBytes)
                responseMessage = self.messageSerializer.fromBytes(messageBytes)

                return responseMessage
        except ConnectionRefusedError:
            return None
