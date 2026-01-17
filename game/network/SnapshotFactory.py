from game.model.network.Person import Person
from game.network.Snapshot import Snapshot


class SnapshotFactory:

    def makeClientSnapshot(self, clientGameState):
        snapshot = Snapshot()
        snapshot.player = Person()
        snapshot.player.id = clientGameState.player.id
        snapshot.player.centerPoint = clientGameState.player.currentCenterPoint.copy()
        snapshot.player.lookDirection = clientGameState.player.lookDirection.copy()

        return snapshot

    def makeServerSnapshot(self, serverGameState):
        snapshot = Snapshot()

        return snapshot
