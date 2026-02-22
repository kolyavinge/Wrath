from game.lib.Dictionary import Dictionary
from game.lib.Set import Set
from game.model.snapshot.SnapshotDiff import SnapshotDiff


class SnapshotDiffLogic:

    # clientPlayerId - id клиента которому предназначается этот diff
    def getSnapshotsDiff(self, snapshotOld, snapshotNew, clientPlayerId=None):
        diff = SnapshotDiff()

        if hasattr(snapshotNew, "person"):
            if snapshotOld.person != snapshotNew.person:
                diff.person = snapshotNew.person

        if hasattr(snapshotNew, "players"):
            assert clientPlayerId != None
            for playerId, player in snapshotNew.players.items():
                if playerId == clientPlayerId:
                    if playerId in snapshotOld.players and player != snapshotOld.players[playerId]:
                        diff.player = player
                    else:
                        break

        if hasattr(snapshotNew, "allPerson"):
            assert clientPlayerId != None
            changedEnemies = []
            addedEnemyIds = []
            for personId, newPerson in snapshotNew.allPerson.items():
                if personId != clientPlayerId:
                    if personId in snapshotOld.allPerson:
                        if newPerson != snapshotOld.allPerson[personId]:
                            changedEnemies.append(newPerson)
                    else:
                        addedEnemyIds.append(personId)
                        changedEnemies.append(newPerson)

            if len(changedEnemies) > 0:
                diff.enemies = changedEnemies
            if len(addedEnemyIds) > 0:
                diff.addedEnemyIds = addedEnemyIds

        if hasattr(snapshotNew, "respawnedPerson"):
            changedRespawnedPerson = Set.getAddedItems(snapshotOld.respawnedPerson, snapshotNew.respawnedPerson)
            if len(changedRespawnedPerson) > 0:
                diff.respawnedPerson = changedRespawnedPerson

        if hasattr(snapshotNew, "bullets"):
            if clientPlayerId is not None:
                addedBullets = Dictionary.getAddedItemsWithFilter(
                    snapshotOld.bullets, snapshotNew.bullets, lambda _, newBullet: newBullet.personId != clientPlayerId
                )
            else:
                addedBullets = Dictionary.getAddedItems(snapshotOld.bullets, snapshotNew.bullets)

            if len(addedBullets) > 0:
                diff.addedBullets = addedBullets

        if hasattr(snapshotNew, "rays"):

            if clientPlayerId is not None:
                if len(snapshotNew.rays) > 0:
                    pass
                addedRays = Dictionary.getAddedItemsWithFilter(
                    snapshotOld.rays, snapshotNew.rays, lambda _, newRay: newRay.personId != clientPlayerId
                )
                removedRays = Dictionary.getRemovedItemsWithFilter(
                    snapshotOld.rays, snapshotNew.rays, lambda _, oldRay: oldRay.personId != clientPlayerId
                )
            else:
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
