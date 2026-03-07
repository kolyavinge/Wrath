from game.model.snapshot.SnapshotPersonDiff import SnapshotPersonDiff


class SnapshotPersonDiffLogic:

    def getSnapshotsDiff(self, oldSnapshotPerson, newSnapshotPerson):
        diff = SnapshotPersonDiff()
        diff.id = newSnapshotPerson.id

        if newSnapshotPerson.centerPoint is not None and oldSnapshotPerson.centerPoint != newSnapshotPerson.centerPoint:
            diff.centerPoint = newSnapshotPerson.centerPoint

        if newSnapshotPerson.yawRadians is not None and oldSnapshotPerson.yawRadians != newSnapshotPerson.yawRadians:
            diff.yawRadians = newSnapshotPerson.yawRadians

        if newSnapshotPerson.pitchRadians is not None and oldSnapshotPerson.pitchRadians != newSnapshotPerson.pitchRadians:
            diff.pitchRadians = newSnapshotPerson.pitchRadians

        if newSnapshotPerson.health is not None and oldSnapshotPerson.health != newSnapshotPerson.health:
            diff.health = newSnapshotPerson.health

        if newSnapshotPerson.jumpingValue is not None and oldSnapshotPerson.jumpingValue != newSnapshotPerson.jumpingValue:
            diff.jumpingValue = newSnapshotPerson.jumpingValue

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

        if person.jumpingValue is not None:
            diff.jumpingValue = person.jumpingValue

        return diff
