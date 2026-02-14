from socket import AF_INET, SOCK_DGRAM, socket
from threading import Thread

from game.network.Message import Message
from game.network.MessageSerializer import MessageSerializer
from game.network.SendMessageResult import SendMessageResult


class NetMessageChannel:

    def __init__(self, portForSending, portForReceiving):
        self.portForSending = portForSending
        self.portForReceiving = portForReceiving
        self.messageSerializer = MessageSerializer()
        self.receivedMessages = []
        self.isListenerRunning = False

    def open(self):
        self.runListenerAsync()

    def close(self):
        self.isListenerRunning = False

    def sendMessage(self, message):
        with socket(AF_INET, SOCK_DGRAM) as udpSender:
            messageBytes, messageLength = self.messageSerializer.toBytes(message)
            udpSender.sendto(messageBytes[:messageLength], ("127.0.0.1", self.portForSending))
            acknowledgeByte = udpSender.recv(1)
            if acknowledgeByte[0] == SendMessageResult.sended:
                return SendMessageResult.sended
            else:
                return SendMessageResult.notSended

    def receiveMessageOrNone(self):
        if len(self.receivedMessages) == 0:
            return None

        message = self.receivedMessages[0]
        self.receivedMessages.clear()

        return message

    def runListenerAsync(self):
        self.thread = Thread(target=self.runListener)
        self.thread.start()

    def runListener(self):
        self.isListenerRunning = True
        with socket(AF_INET, SOCK_DGRAM) as udpListener:
            udpListener.bind(("127.0.0.1", self.portForReceiving))
            while self.isListenerRunning:
                messageBytes, serverAddress = udpListener.recvfrom(Message.maxMessageSizeBytes)
                message = self.messageSerializer.fromBytes(messageBytes)
                self.receivedMessages.append(message)
                sentBytes = udpListener.sendto(SendMessageResult.sendedAsBytes, serverAddress)
                assert sentBytes == 1
