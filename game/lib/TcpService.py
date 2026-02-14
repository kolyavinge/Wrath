from socket import AF_INET, SOCK_STREAM, socket
from threading import Thread


class TcpService:

    def runAsync(self):
        self.thread = Thread(target=self.run)
        self.thread.start()

    def run(self):
        with socket(AF_INET, SOCK_STREAM) as tcpListener:
            tcpListener.bind(("127.0.0.1", 6464))
            tcpListener.listen()
            self.onBeginListen()
            while True:
                clientSocket, clientAddress = tcpListener.accept()
                with clientSocket:
                    self.accept(clientSocket, clientAddress)

        self.onEndListen()

    def accept(self, clientSocket, clientAddress):
        pass

    def onBeginListen(self):
        pass

    def onEndListen(self):
        pass
