from game.engine.person.PersonTurnLogic import PersonTurnLogic
from game.engine.person.PersonWeaponPositionUpdater import PersonWeaponPositionUpdater
from game.engine.powerup.PowerupLogic import PowerupLogic
from game.engine.weapon.BulletLogic import BulletLogic
from game.engine.weapon.BulletPositionUpdater import BulletPositionUpdater
from game.engine.weapon.DebrisLogic import DebrisLogic
from game.engine.weapon.ExplosionLogic import ExplosionLogic
from game.engine.weapon.RayLogic import RayLogic
from game.engine.weapon.WeaponSelector import WeaponSelector
from game.lib.Query import Query
from game.model.powerup.PowerupType import PowerupType
from game.model.snapshot.SnapshotBullet import WeaponExtraBit
from game.model.weapon.Debris import Debris
from game.model.weapon.Plasma import Plasma
from game.model.weapon.WeaponCollection import WeaponCollection


class GameStateSynchronizer:

    def __init__(
        self,
        personTurnLogic: PersonTurnLogic,
        bulletLogic: BulletLogic,
        debrisLogic: DebrisLogic,
        rayLogic: RayLogic,
        explosionLogic: ExplosionLogic,
        bulletPositionUpdater: BulletPositionUpdater,
        weaponSelector: WeaponSelector,
        personWeaponPositionUpdater: PersonWeaponPositionUpdater,
        powerupLogic: PowerupLogic,
    ):
        self.personTurnLogic = personTurnLogic
        self.bulletLogic = bulletLogic
        self.debrisLogic = debrisLogic
        self.rayLogic = rayLogic
        self.explosionLogic = explosionLogic
        self.bulletPositionUpdater = bulletPositionUpdater
        self.weaponSelector = weaponSelector
        self.personWeaponPositionUpdater = personWeaponPositionUpdater
        self.powerupLogic = powerupLogic

    def applySnapshotDiff(self, gameState, diff):
        if hasattr(diff, "player"):
            self.synchPerson(gameState, diff.player)

        if hasattr(diff, "players"):
            for player in diff.players:
                self.synchPlayer(gameState, player)

        if hasattr(diff, "enemies"):
            for enemy in diff.enemies:
                self.synchPerson(gameState, enemy)

        if hasattr(diff, "respawnedPerson"):
            for person in diff.respawnedPerson:
                self.synchRespawnedPerson(gameState, person)

        if hasattr(diff, "addedBullets"):
            for bullet in diff.addedBullets:
                self.synchAddedBullet(gameState, bullet)

        if hasattr(diff, "addedDebris"):
            for debris in diff.addedDebris:
                self.synchAddedDebris(gameState, debris)

        if hasattr(diff, "addedRays"):
            for ray in diff.addedRays:
                self.synchAddedRay(gameState, ray)

        if hasattr(diff, "removedRayIds"):
            for rayId in diff.removedRayIds:
                self.synchRemovedRay(gameState, rayId)

        if hasattr(diff, "addedPowerups"):
            for powerup in diff.addedPowerups:
                self.synchAddedPowerup(gameState, powerup)

        if hasattr(diff, "removedPowerupIds"):
            for powerupId in diff.removedPowerupIds:
                self.synchRemovedPowerup(gameState, powerupId)

        if hasattr(diff, "pickedupPowerupIds"):
            for powerupId in diff.pickedupPowerupIds:
                self.synchRemovedPowerup(gameState, powerupId)

        if hasattr(diff, "addedPersonBulletCollisions"):
            for bulletCollision in diff.addedPersonBulletCollisions:
                self.synchAddedPersonBulletCollision(gameState, bulletCollision)

        if hasattr(diff, "addedPersonRayCollisions"):
            for rayCollision in diff.addedPersonRayCollisions:
                self.synchAddedPersonRayCollision(gameState, rayCollision)

        if hasattr(diff, "addedPersonFrags"):
            for frags in diff.addedPersonFrags:
                self.synchAddedPersonFrags(gameState, frags)

        if hasattr(diff, "addedPersonDeaths"):
            for deaths in diff.addedPersonDeaths:
                self.synchAddedPersonDeaths(gameState, deaths)

    def synchPerson(self, gameState, diffPerson):
        sychedPerson = gameState.allPersonById[diffPerson.id]
        sychedPerson.moveNextPositionTo(diffPerson.centerPoint)
        self.personTurnLogic.setYawPitchRadians(sychedPerson, diffPerson.yawRadians, diffPerson.pitchRadians)
        sychedPerson.commitNextPosition()
        sychedPerson.health = diffPerson.health

    def synchPlayer(self, gameState, diffPlayer):
        sychedPlayer = gameState.allPersonById[diffPlayer.id]
        sychedPlayer.health = diffPlayer.health

    def synchRespawnedPerson(self, gameState, diffPerson):
        sychedPerson = gameState.allPersonById[diffPerson.id]
        sychedPerson.moveNextPositionTo(diffPerson.centerPoint)
        sychedPerson.commitNextPosition()

    def synchAddedBullet(self, gameState, diffBullet):
        # TODO подумать как при рассинхроне обработать на клиенте тот путь
        # который пуля пролетела на сервере до передачи клиенту
        # сюда же: если у пули перед выстрелом изменилась скорость (Railgun charge)
        person = gameState.allPersonById[diffBullet.personId]
        personItems = gameState.allPersonItems[person]
        isLeftHandWeapon = diffBullet.weaponNumber & WeaponExtraBit.leftHandWeapon > 0
        if isLeftHandWeapon:
            # remove leftHandWeapon bit from weaponNumber
            diffBullet.weaponNumber &= ~WeaponExtraBit.leftHandWeapon
        diffBulletWeaponType = WeaponCollection.getWeaponTypeByNumber(diffBullet.weaponNumber)
        if not personItems.hasWeaponByType(diffBulletWeaponType):
            return
        if personItems.getCurrentWeaponType() != diffBulletWeaponType:
            self.weaponSelector.setWeaponByType(personItems, diffBulletWeaponType)
            self.personWeaponPositionUpdater.updateForPerson(person, personItems)
        if diffBulletWeaponType.defaultCount == 2:
            if isLeftHandWeapon:
                personItems.setLeftHandWeaponAsCurrent()
            else:
                personItems.setRightHandWeaponAsCurrent()
        newBullet = self.bulletLogic.makeBullet(gameState, person, personItems.currentWeapon, diffBullet.id)
        newBullet.direction = diffBullet.direction.copy()
        # newBullet.velocityValue = diffBullet.velocityValue
        # newBullet.velocity.setLength(diffBullet.velocityValue)
        self.bulletPositionUpdater.moveBulletNextPositionTo(gameState, newBullet, diffBullet.position)
        self.bulletPositionUpdater.commitBulletNextPosition(newBullet, gameState.visibilityTree)
        diffBulletWeapon = personItems.getWeaponByTypeOrNone(diffBulletWeaponType)
        gameState.updateStatistic.firedWeapons.append((person, diffBulletWeapon))

    def synchAddedDebris(self, gameState, diffDebris):
        person = gameState.allPersonById[diffDebris.personId]
        self.debrisLogic.makeDebrisManually(gameState, diffDebris.id, Debris, person, diffDebris.position, diffDebris.direction)

    def synchAddedRay(self, gameState, diffRay):
        person = gameState.allPersonById[diffRay.personId]
        personItems = gameState.allPersonItems[person]
        weapon = personItems.getWeaponByTypeOrNone(Plasma)
        if weapon is None:
            return
        if personItems.currentWeapon != weapon:
            self.weaponSelector.setWeaponByType(personItems, type(weapon))
            self.personWeaponPositionUpdater.updateForPerson(person, personItems)
        self.rayLogic.makeRay(gameState, person, weapon, diffRay.id)

    def synchRemovedRay(self, gameState, diffRayId):
        ray = Query(gameState.rays).firstOrNone(lambda x: x.id == diffRayId)
        if ray is not None:
            self.rayLogic.removeRay(gameState, ray)

    def synchAddedPowerup(self, gameState, diffPowerup):
        powerupType = PowerupType.getPowerupTypeFromKind(diffPowerup.kind)
        self.powerupLogic.makePowerup(gameState, powerupType, diffPowerup.position, diffPowerup.id)

    def synchRemovedPowerup(self, gameState, diffPowerupId):
        powerup = Query(gameState.powerups).firstOrNone(lambda x: x.id == diffPowerupId)
        if powerup is not None:
            self.powerupLogic.removePowerup(gameState, powerup)

    def synchAddedPersonBulletCollision(self, gameState, diffBulletCollision):
        bullet = gameState.removedBullets.getByKeyOrNone(diffBulletCollision.bulletId)
        if bullet is None and diffBulletCollision.bulletId in gameState.bulletsById:
            bullet = gameState.bulletsById[diffBulletCollision.bulletId]
        else:
            return
        damagedPerson = gameState.allPersonById[diffBulletCollision.damagedPersonId]
        gameState.collisionData.personBullet[damagedPerson] = bullet
        bullet.damagedObject = damagedPerson
        bullet.currentPosition = diffBulletCollision.collisionPoint.copy()
        bullet.nextPosition = bullet.currentPosition
        self.bulletLogic.removeBullet(gameState, bullet)
        self.explosionLogic.makeExplosion(gameState, bullet)

    def synchAddedPersonRayCollision(self, gameState, diffRayCollision):
        ray = Query(gameState.rays).firstOrNone(lambda x: x.id == diffRayCollision.rayId)
        if ray is None:
            return
        damagedPerson = gameState.allPersonById[diffRayCollision.damagedPersonId]
        gameState.collisionData.personRay[damagedPerson] = ray
        ray.damagedObject = damagedPerson
        ray.stopOnPosition(diffRayCollision.collisionPoint)

    def synchAddedPersonFrags(self, gameState, diffFrags):
        person = gameState.allPersonById[diffFrags.personId]
        gameState.personFragStatistic[person].frags = diffFrags.value

    def synchAddedPersonDeaths(self, gameState, diffDeaths):
        person = gameState.allPersonById[diffDeaths.personId]
        gameState.personFragStatistic[person].deaths = diffDeaths.value
