class ServerSnapshot:

    lastId = 0

    @staticmethod
    def makeEmpty():
        empty = ServerSnapshot()
        empty.enemies = []
        empty.bullets = []
        empty.powerups = {}

        return empty

    def __init__(self):
        self.id = ServerSnapshot.lastId
        ServerSnapshot.lastId += 1
        self.acknowledged = False
        self.enemies = None
        self.bullets = None
        self.powerups = None
