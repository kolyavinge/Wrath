from game.anx.ConfigManager import ConfigManager
from game.lib.TcpService import TcpService
from game.network.contracts import ConnectToServerResponse
from game.network.Message import Message, MessageType
from game.network.MessageSerializer import MessageSerializer
from game.network.ServerConnectionLogic import ServerConnectionLogic


class GameService:

    def __init__(
        self,
        messageSerializer: MessageSerializer,
        serverConnectionLogic: ServerConnectionLogic,
        configManager: ConfigManager,
    ):
        self.messageSerializer = messageSerializer
        self.serverConnectionLogic = serverConnectionLogic
        self.serverAddress = configManager.serverAddress
        self.serverPort = configManager.serverPort
        self.tcpService = TcpService(configManager.serverAddress, configManager.serverPort)
        self.tcpService.receive = self.receive
        self.tcpService.onBeginListen = self.onBeginListen
        self.tcpService.onEndListen = self.onEndListen

    def runAsync(self):
        self.tcpService.runAsync()

    def receive(self, clientSocket, clientAddressAndPort):
        messageBytes = clientSocket.recv(Message.maxMessageSizeBytes)
        requestMessage = self.messageSerializer.fromBytes(messageBytes)
        responseMessage = self.processMessage(requestMessage, clientAddressAndPort)
        messageBytes, messageLength = self.messageSerializer.toBytes(responseMessage)
        clientSocket.sendall(messageBytes[:messageLength])

    def processMessage(self, requestMessage, clientAddressAndPort):
        if requestMessage.type == MessageType.connectToServerRequest:
            print("GameService has received connection request.")
            playerId, portForSendingToServer, portForReceivingFromServer = self.serverConnectionLogic.connectByNet(clientAddressAndPort)
            print(f"Client connected: id={playerId}, portSendToServer={portForSendingToServer}, portReceiveFromServer={portForReceivingFromServer}.")
            response = ConnectToServerResponse(playerId, portForSendingToServer, portForReceivingFromServer)
            responseMessage = Message(MessageType.connectToServerResponse, response)

            return responseMessage
        else:
            raise Exception("Wrong message type.")

    def onBeginListen(self):
        print(f"GameService is running on {self.serverAddress}:{self.serverPort}.")

    def onEndListen(self):
        print("GameService was stopped.")
