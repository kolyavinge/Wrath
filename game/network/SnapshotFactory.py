from game.model.snapshot.Person import Person
from game.network.Snapshot import Snapshot


class SnapshotFactory:

    def makeClientSnapshot(self, clientGameState):
        snapshot = Snapshot()
        snapshot.player = self.makeSnapshotPersonFor(clientGameState.player)

        return snapshot

    def makeServerSnapshot(self, serverGameState):
        snapshot = Snapshot()
        snapshot.enemies = [self.makeSnapshotPersonFor(enemy) for enemy in serverGameState.enemies]

        return snapshot

    def makeSnapshotPersonFor(self, person):
        snapshotPerson = Person()
        snapshotPerson.id = person.id
        snapshotPerson.centerPoint = person.currentCenterPoint.copy()
        snapshotPerson.yawRadians = person.yawRadians
        snapshotPerson.pitchRadians = person.pitchRadians

        return snapshotPerson
