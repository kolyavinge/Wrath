from queue import Queue
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
        self.receivedMessages = Queue()
        self.isListenerRunning = False
        self.udpListener = None

    def open(self):
        self.runListenerAsync()

    def close(self):
        self.isListenerRunning = False
        if self.udpListener is not None:
            self.udpListener.close()

    def sendMessage(self, message):
        try:
            udpSender = socket(AF_INET, SOCK_DGRAM)
            messageBytes, messageLength = self.messageSerializer.toBytes(message)
            udpSender.sendto(messageBytes[:messageLength], ("127.0.0.1", self.portForSending))
            acknowledgeByte = udpSender.recv(1)
            if acknowledgeByte[0] == SendMessageResult.sended:
                return SendMessageResult.sended
            else:
                return SendMessageResult.notSended
        except ConnectionResetError:
            return SendMessageResult.notSended
        finally:
            udpSender.close()

    def receiveMessageOrNone(self):
        if not self.receivedMessages.empty():
            return self.receivedMessages.get()
        else:
            return None

    def runListenerAsync(self):
        self.thread = Thread(target=self.runListener)
        self.thread.start()

    def runListener(self):
        self.isListenerRunning = True
        self.udpListener = socket(AF_INET, SOCK_DGRAM)
        self.udpListener.bind(("127.0.0.1", self.portForReceiving))
        while self.isListenerRunning:
            messageBytes, serverAddress = self.udpListener.recvfrom(Message.maxMessageSizeBytes)
            message = self.messageSerializer.fromBytes(messageBytes)
            sentBytes = self.udpListener.sendto(SendMessageResult.sendedAsBytes, serverAddress)
            assert sentBytes == 1
            self.receivedMessages.put(message)
