from socket import AF_INET, SOCK_STREAM, socket
from threading import Thread


class TcpService:

    def __init__(self, serverAddress, serverPort):
        self.serverAddress = serverAddress
        self.serverPort = serverPort

    def runAsync(self):
        self.thread = Thread(target=self.run)
        self.thread.start()

    def run(self):
        with socket(AF_INET, SOCK_STREAM) as tcpListener:
            tcpListener.bind((self.serverAddress, self.serverPort))
            tcpListener.listen()
            self.onBeginListen()
            while True:
                clientSocket, clientAddress = tcpListener.accept()
                with clientSocket:
                    self.receive(clientSocket, clientAddress)

        self.onEndListen()

    def receive(self, clientSocket, clientAddress):
        pass

    def onBeginListen(self):
        pass

    def onEndListen(self):
        pass
