from game.lib.Dictionary import Dictionary
from game.model.snapshot.SnapshotDiff import SnapshotDiff


class SnapshotDiffLogic:

    def getSnapshotsDiff(self, snapshotOld, snapshotNew):
        diff = SnapshotDiff()

        if hasattr(snapshotNew, "player"):
            if snapshotOld.player != snapshotNew.player:
                diff.player = snapshotNew.player

        if hasattr(snapshotNew, "enemies"):
            if len(snapshotOld.enemies) == len(snapshotNew.enemies):
                diff.enemies = []
                i = 0
                while i < len(snapshotOld.enemies):
                    if snapshotOld.enemies[i] != snapshotNew.enemies[i]:
                        diff.enemies.append(snapshotNew.enemies[i])
                    i += 1
            else:
                diff.enemies = snapshotNew.enemies

        if hasattr(snapshotNew, "bullets"):
            diff.bullets = snapshotNew.bullets

        if hasattr(snapshotNew, "powerups"):
            addedPowerups = Dictionary.getAddedItems(snapshotOld.powerups, snapshotNew.powerups)
            removedPowerups = Dictionary.getRemovedItems(snapshotOld.powerups, snapshotNew.powerups)
            if len(addedPowerups) > 0:
                diff.addedPowerups = addedPowerups
            if len(removedPowerups) > 0:
                diff.removedPowerupIds = [p.id for p in removedPowerups]

        return diff
