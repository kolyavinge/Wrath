from game.model.network.Person import Person
from game.network.Snapshot import Snapshot


class SnapshotFactory:

    def makeClientSnapshot(self, clientGameState):
        snapshot = Snapshot()
        snapshot.player = Person()
        snapshot.player.id = clientGameState.player.id
        snapshot.player.centerPoint = clientGameState.player.currentCenterPoint.copy()
        snapshot.player.yawRadians = clientGameState.player.yawRadians
        snapshot.player.pitchRadians = clientGameState.player.pitchRadians

        return snapshot

    def makeServerSnapshot(self, serverGameState):
        snapshot = Snapshot()

        return snapshot
