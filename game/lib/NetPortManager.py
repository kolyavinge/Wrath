from socket import *


class NetPortManager:

    def getFreePort(self):
        with socket(AF_INET, SOCK_STREAM) as s:
            s.bind(("", 0))
            return s.getsockname()[1]
