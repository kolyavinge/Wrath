from game.model.snapshot.SnapshotPerson import SnapshotPerson


class ClientSnapshot:

    lastId = 0

    @staticmethod
    def makeEmpty():
        empty = ClientSnapshot()
        empty.player = SnapshotPerson()
        empty.bullets = {}
        empty.debris = {}
        empty.notPickedupPowerupIds = {}

        return empty

    def __init__(self):
        self.id = ClientSnapshot.lastId
        ClientSnapshot.lastId += 1
        self.acknowledged = False
        self.player = None
        self.bullets = None
        self.debris = None
        self.notPickedupPowerupIds = None
