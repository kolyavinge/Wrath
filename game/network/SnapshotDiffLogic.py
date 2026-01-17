from game.network.Snapshot import SnapshotDiff


class SnapshotDiffLogic:

    def getSnapshotsDiff(self, snapshotOld, snapshotNew):
        diff = SnapshotDiff()

        if hasattr(snapshotNew, "player"):
            if hasattr(snapshotOld, "player"):
                if snapshotOld.player != snapshotNew.player:
                    diff.player = snapshotNew.player
            else:
                diff.player = snapshotNew.player

        return diff
