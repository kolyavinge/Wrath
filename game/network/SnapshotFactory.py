from game.model.network.Person import Person
from game.network.Snapshot import Snapshot


class SnapshotFactory:

    def __init__(self):
        self.lastSnapshotId = 0

    def makeClientSnapshot(self, clientGameState):
        self.lastSnapshotId += 1
        snapshot = Snapshot(self.lastSnapshotId)
        snapshot.player = Person()
        # snapshot.player.id = clientGameState.player.id
        snapshot.player.centerPoint = clientGameState.player.currentCenterPoint.copy()
        snapshot.player.lookDirection = clientGameState.player.lookDirection.copy()

        return snapshot

    def makeServerSnapshot(self, serverGameState):
        self.lastSnapshotId += 1
        snapshot = Snapshot(self.lastSnapshotId)

        return snapshot
