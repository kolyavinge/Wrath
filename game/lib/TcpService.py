from socket import AF_INET, SOCK_STREAM, socket
from threading import Thread


class TcpService:

    def __init__(self, serverAddress, serverPort):
        self.serverAddress = serverAddress
        self.serverPort = serverPort
        self.tcpListener = None
        self.isRunning = False

    def runAsync(self):
        self.thread = Thread(target=self.run)
        self.thread.start()

    def run(self):
        with socket(AF_INET, SOCK_STREAM) as tcpListener:
            self.tcpListener = tcpListener
            tcpListener.bind((self.serverAddress, self.serverPort))
            tcpListener.listen()
            self.isRunning = True
            self.onBeginListen()
            while self.isRunning:
                try:
                    clientSocket, clientAddress = tcpListener.accept()
                    with clientSocket:
                        self.receive(clientSocket, clientAddress)
                except Exception:
                    pass

        self.onEndListen()

    def receive(self, clientSocket, clientAddress):
        pass

    def stop(self):
        if self.tcpListener is not None:
            self.isRunning = False
            self.tcpListener.close()
            self.tcpListener = None

    def onBeginListen(self):
        pass

    def onEndListen(self):
        pass
