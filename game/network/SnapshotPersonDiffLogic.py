from game.model.snapshot.SnapshotPersonDiff import SnapshotPersonDiff


class SnapshotPersonDiffLogic:

    def getSnapshotsDiff(self, oldSnapshotPerson, newSnapshotPerson):
        diff = SnapshotPersonDiff()
        diff.id = newSnapshotPerson.id

        if oldSnapshotPerson.centerPoint != newSnapshotPerson.centerPoint:
            diff.centerPoint = newSnapshotPerson.centerPoint

        if oldSnapshotPerson.yawRadians != newSnapshotPerson.yawRadians:
            diff.yawRadians = newSnapshotPerson.yawRadians

        if oldSnapshotPerson.pitchRadians != newSnapshotPerson.pitchRadians:
            diff.pitchRadians = newSnapshotPerson.pitchRadians

        if oldSnapshotPerson.health != newSnapshotPerson.health:
            diff.health = newSnapshotPerson.health

        return diff

    def makeDiffFromPerson(self, person):
        diff = SnapshotPersonDiff()
        diff.id = person.id

        if person.centerPoint is not None:
            diff.centerPoint = person.centerPoint

        if person.yawRadians is not None:
            diff.yawRadians = person.yawRadians

        if person.pitchRadians is not None:
            diff.pitchRadians = person.pitchRadians

        if person.health is not None:
            diff.health = person.health

        return diff
