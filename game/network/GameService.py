from socket import AF_INET, SOCK_STREAM, socket
from threading import Thread

from game.lib.NetPortManager import NetPortManager
from game.network.contracts import ConnectToServerResponse
from game.network.Message import Message, MessageType
from game.network.MessageSerializer import MessageSerializer
from game.network.ServerConnector import ServerConnector


class GameService:

    def __init__(
        self,
        messageSerializer: MessageSerializer,
        serverConnector: ServerConnector,
        netPortManager: NetPortManager,
    ):
        self.messageSerializer = messageSerializer
        self.serverConnector = serverConnector
        self.netPortManager = netPortManager

    def runAsync(self):
        self.thread = Thread(target=self.run)
        self.thread.start()

    def run(self):
        with socket(AF_INET, SOCK_STREAM) as tcpListener:
            tcpListener.bind(("127.0.0.1", 6464))
            tcpListener.listen()
            print("GameService is running")
            while True:
                clientSocket, clientAddress = tcpListener.accept()
                with clientSocket:
                    while True:
                        messageLengthBytes = clientSocket.recv(Message.byteMessageSize)
                        messageLength = int.from_bytes(messageLengthBytes)
                        if messageLength == 0:
                            break
                        messageBytes = clientSocket.recv(messageLength)
                        requestMessage = self.messageSerializer.fromBytes(messageBytes)
                        responseMessage = self.processMessage(requestMessage)
                        messageBytes, messageLength = self.messageSerializer.toBytes(responseMessage)
                        clientSocket.sendall(messageLength.to_bytes(Message.byteMessageSize))
                        clientSocket.sendall(messageBytes[:messageLength])

        print("GameService was stopped")

    def processMessage(self, requestMessage):
        if requestMessage.type == MessageType.connectToServerRequest:
            response = ConnectToServerResponse()
            responseMessage = Message(MessageType.connectToServerResponse, response)

            return responseMessage
        else:
            raise Exception("Wrong message type.")
