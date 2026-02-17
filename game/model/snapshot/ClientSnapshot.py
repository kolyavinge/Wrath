from game.model.snapshot.SnapshotPerson import SnapshotPerson


class ClientSnapshot:

    lastId = 0

    @staticmethod
    def makeEmpty():
        empty = ClientSnapshot()
        empty.person = SnapshotPerson()
        empty.bullets = {}
        empty.debris = {}
        empty.rays = {}
        empty.notPickedupPowerupIds = {}

        return empty

    def __init__(self):
        self.id = ClientSnapshot.lastId
        ClientSnapshot.lastId += 1
        self.acknowledged = False
        self.person = None
        self.bullets = None
        self.debris = None
        self.rays = None
        self.notPickedupPowerupIds = None
