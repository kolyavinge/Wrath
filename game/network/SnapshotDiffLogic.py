from game.lib.Dictionary import Dictionary
from game.lib.Set import Set
from game.model.snapshot.SnapshotDiff import SnapshotDiff
from game.network.SnapshotPersonDiffLogic import SnapshotPersonDiffLogic


class SnapshotDiffLogic:

    def __init__(
        self,
        snapshotPersonDiffLogic: SnapshotPersonDiffLogic,
    ):
        self.snapshotPersonDiffLogic = snapshotPersonDiffLogic

    # clientPlayerId - id клиента которому предназначается этот diff
    def getSnapshotsDiff(self, snapshotOld, snapshotNew, clientPlayerId=None):
        diff = SnapshotDiff()

        if hasattr(snapshotNew, "person"):
            personDiff = self.snapshotPersonDiffLogic.getSnapshotsDiff(snapshotOld.person, snapshotNew.person)
            if not personDiff.isEmpty():
                diff.person = personDiff

        if hasattr(snapshotNew, "players"):
            assert clientPlayerId is not None
            for playerId, player in snapshotNew.players.items():
                if playerId != clientPlayerId:
                    continue
                if playerId not in snapshotOld.players:
                    break
                personDiff = self.snapshotPersonDiffLogic.getSnapshotsDiff(snapshotOld.players[playerId], player)
                if not personDiff.isEmpty():
                    diff.player = personDiff
                    break

        if hasattr(snapshotNew, "allPerson"):
            assert clientPlayerId is not None
            changedEnemies = []
            addedEnemyIds = []
            for personId, newPerson in snapshotNew.allPerson.items():
                if personId == clientPlayerId:
                    continue
                if personId in snapshotOld.allPerson:
                    personDiff = self.snapshotPersonDiffLogic.getSnapshotsDiff(snapshotOld.allPerson[personId], newPerson)
                    if not personDiff.isEmpty():
                        changedEnemies.append(personDiff)
                else:
                    addedEnemyIds.append(personId)
                    changedEnemies.append(self.snapshotPersonDiffLogic.makeDiffFromPerson(newPerson))

            removedEnemies = Dictionary.getRemovedItems(snapshotOld.allPerson, snapshotNew.allPerson)

            if len(changedEnemies) > 0:
                diff.enemies = changedEnemies
            if len(addedEnemyIds) > 0:
                diff.addedEnemyIds = addedEnemyIds
            if len(removedEnemies) > 0:
                diff.removedEnemyIds = [enemy.id for enemy in removedEnemies]

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
