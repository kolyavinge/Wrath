class ServerSnapshot:

    lastId = 0

    @staticmethod
    def makeEmpty():
        empty = ServerSnapshot()
        empty.enemies = []
        empty.bullets = {}
        empty.debris = {}
        empty.rays = {}
        empty.powerups = {}

        return empty

    def __init__(self):
        self.id = ServerSnapshot.lastId
        ServerSnapshot.lastId += 1
        self.acknowledged = False
        self.enemies = None
        self.bullets = None
        self.debris = None
        self.rays = None
        self.powerups = None
