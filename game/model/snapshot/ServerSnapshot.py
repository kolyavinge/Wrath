class ServerSnapshot:

    lastId = 0

    @staticmethod
    def makeEmpty():
        empty = ServerSnapshot()
        empty.players = set()
        empty.allPerson = {}
        empty.respawnedPerson = set()
        empty.bullets = {}
        empty.debris = {}
        empty.rays = {}
        empty.powerups = {}
        empty.personBulletCollisions = {}
        empty.personRayCollisions = {}
        empty.personFrags = set()
        empty.personDeaths = set()

        return empty

    def __init__(self):
        self.id = ServerSnapshot.lastId
        ServerSnapshot.lastId += 1
        self.acknowledged = False
        self.players = None
        self.allPerson = None
        self.respawnedPerson = None
        self.bullets = None
        self.debris = None
        self.rays = None
        self.powerups = None
        self.personBulletCollisions = None
        self.personRayCollisions = None
        self.personFrags = None
        self.personDeaths = None
