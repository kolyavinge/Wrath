from game.lib.Dictionary import Dictionary
from game.lib.Set import Set
from game.model.snapshot.SnapshotDiff import SnapshotDiff


class SnapshotDiffLogic:

    def getSnapshotsDiff(self, snapshotOld, snapshotNew):
        diff = SnapshotDiff()

        if hasattr(snapshotNew, "player"):
            if snapshotOld.player != snapshotNew.player:
                diff.player = snapshotNew.player

        if hasattr(snapshotNew, "players"):
            changedPlayers = Set.getAddedItems(snapshotOld.players, snapshotNew.players)
            if len(changedPlayers) > 0:
                diff.players = changedPlayers

        if hasattr(snapshotNew, "enemies"):
            changedEnemies = Set.getAddedItems(snapshotOld.enemies, snapshotNew.enemies)
            if len(changedEnemies) > 0:
                diff.enemies = changedEnemies

        if hasattr(snapshotNew, "bullets"):
            addedBullets = Dictionary.getAddedItems(snapshotOld.bullets, snapshotNew.bullets)
            if len(addedBullets) > 0:
                diff.addedBullets = addedBullets

        if hasattr(snapshotNew, "debris"):
            addedDebris = Dictionary.getAddedItems(snapshotOld.debris, snapshotNew.debris)
            if len(addedDebris) > 0:
                diff.addedDebris = addedDebris

        if hasattr(snapshotNew, "rays"):
            addedRays = Dictionary.getAddedItems(snapshotOld.rays, snapshotNew.rays)
            removedRays = Dictionary.getRemovedItems(snapshotOld.rays, snapshotNew.rays)
            if len(addedRays) > 0:
                diff.addedRays = addedRays
            if len(removedRays) > 0:
                diff.removedRayIds = [ray.id for ray in removedRays]

        if hasattr(snapshotNew, "powerups"):
            addedPowerups = Dictionary.getAddedItems(snapshotOld.powerups, snapshotNew.powerups)
            removedPowerups = Dictionary.getRemovedItems(snapshotOld.powerups, snapshotNew.powerups)
            if len(addedPowerups) > 0:
                diff.addedPowerups = addedPowerups
            if len(removedPowerups) > 0:
                diff.removedPowerupIds = [p.id for p in removedPowerups]

        if hasattr(snapshotNew, "notPickedupPowerupIds"):
            pickedupPowerupIds = Set.getRemovedItems(snapshotOld.notPickedupPowerupIds, snapshotNew.notPickedupPowerupIds)
            if len(pickedupPowerupIds) > 0:
                diff.pickedupPowerupIds = pickedupPowerupIds

        if hasattr(snapshotNew, "personBulletCollisions"):
            addedPersonBulletCollisions = Dictionary.getAddedItems(snapshotOld.personBulletCollisions, snapshotNew.personBulletCollisions)
            if len(addedPersonBulletCollisions) > 0:
                diff.addedPersonBulletCollisions = addedPersonBulletCollisions

        if hasattr(snapshotNew, "personRayCollisions"):
            addedPersonRayCollisions = Dictionary.getAddedItems(snapshotOld.personRayCollisions, snapshotNew.personRayCollisions)
            if len(addedPersonRayCollisions) > 0:
                diff.addedPersonRayCollisions = addedPersonRayCollisions

        if hasattr(snapshotNew, "personFrags"):
            addedPersonDeaths = Set.getAddedItems(snapshotOld.personFrags, snapshotNew.personFrags)
            if len(addedPersonDeaths) > 0:
                diff.addedPersonFrags = addedPersonDeaths

        if hasattr(snapshotNew, "personDeaths"):
            addedPersonDeaths = Set.getAddedItems(snapshotOld.personDeaths, snapshotNew.personDeaths)
            if len(addedPersonDeaths) > 0:
                diff.addedPersonDeaths = addedPersonDeaths

        return diff
