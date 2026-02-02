from game.engine.person.PersonTurnLogic import PersonTurnLogic
from game.engine.person.PersonWeaponPositionUpdater import PersonWeaponPositionUpdater
from game.engine.powerup.PowerupLogic import PowerupLogic
from game.engine.weapon.BulletLogic import BulletLogic
from game.engine.weapon.BulletPositionUpdater import BulletPositionUpdater
from game.engine.weapon.DebrisLogic import DebrisLogic
from game.engine.weapon.RayLogic import RayLogic
from game.engine.weapon.WeaponSelector import WeaponSelector
from game.lib.Query import Query
from game.model.powerup.PowerupType import PowerupType
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
        bulletPositionUpdater: BulletPositionUpdater,
        weaponSelector: WeaponSelector,
        personWeaponPositionUpdater: PersonWeaponPositionUpdater,
        powerupLogic: PowerupLogic,
    ):
        self.personTurnLogic = personTurnLogic
        self.bulletLogic = bulletLogic
        self.debrisLogic = debrisLogic
        self.rayLogic = rayLogic
        self.bulletPositionUpdater = bulletPositionUpdater
        self.weaponSelector = weaponSelector
        self.personWeaponPositionUpdater = personWeaponPositionUpdater
        self.powerupLogic = powerupLogic

    def applySnapshotDiff(self, gameState, diff):
        if hasattr(diff, "player"):
            self.synchPerson(gameState, diff.player)

        if hasattr(diff, "enemies"):
            for enemy in diff.enemies:
                self.synchPerson(gameState, enemy)

        if hasattr(diff, "addedBullets"):
            for bullet in diff.addedBullets:
                self.synchAddedBullet(gameState, bullet)

        if hasattr(diff, "addedDebris"):
            for debris in diff.addedDebris:
                self.synchAddedDebris(gameState, debris)

        if hasattr(diff, "addedRays"):
            for ray in diff.addedRays:
                self.synchAddedRay(gameState, ray)

        if hasattr(diff, "removedRayPersonIds"):
            for rayPersonId in diff.removedRayPersonIds:
                self.synchRemovedRay(gameState, rayPersonId)

        if hasattr(diff, "addedPowerups"):
            for powerup in diff.addedPowerups:
                self.synchAddedPowerup(gameState, powerup)

        if hasattr(diff, "removedPowerupIds"):
            for powerupId in diff.removedPowerupIds:
                self.synchRemovedPowerup(gameState, powerupId)

        if hasattr(diff, "pickedupPowerupIds"):
            for powerupId in diff.pickedupPowerupIds:
                self.synchRemovedPowerup(gameState, powerupId)

    def synchPerson(self, gameState, diffPerson):
        sychedPerson = gameState.allPersonById[diffPerson.id]
        sychedPerson.moveNextPositionTo(diffPerson.centerPoint)
        self.personTurnLogic.setYawPitchRadians(sychedPerson, diffPerson.yawRadians, diffPerson.pitchRadians)
        sychedPerson.commitNextPosition()

    def synchAddedBullet(self, gameState, diffBullet):
        person = gameState.allPersonById[diffBullet.personId]
        personItems = gameState.allPersonItems[person]
        diffBulletWeapon = personItems.getWeaponByTypeOrNone(WeaponCollection.getWeaponTypeByNumber(diffBullet.weaponNumber))
        if diffBulletWeapon is None:
            return
        if personItems.currentWeapon != diffBulletWeapon:
            self.weaponSelector.setWeaponByType(personItems, type(diffBulletWeapon))
            self.personWeaponPositionUpdater.updateForPerson(person, personItems)
        newBullet = self.bulletLogic.makeBullet(gameState, person, personItems.currentWeapon, diffBullet.id)
        newBullet.direction = diffBullet.direction.copy()
        # newBullet.velocityValue = diffBullet.velocityValue
        # newBullet.velocity.setLength(diffBullet.velocityValue)
        self.bulletPositionUpdater.moveBulletNextPositionTo(gameState, newBullet, diffBullet.position)
        self.bulletPositionUpdater.commitBulletNextPosition(newBullet, gameState.visibilityTree)

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
        self.rayLogic.makeRay(gameState, person, weapon)

    def synchRemovedRay(self, gameState, diffRayPersonId):
        ray = Query(gameState.rays).firstOrNone(lambda x: x.ownerPerson.id == diffRayPersonId)
        if ray is not None:
            self.rayLogic.removeRay(gameState, ray)

    def synchAddedPowerup(self, gameState, diffPowerup):
        powerupType = PowerupType.getPowerupTypeFromKind(diffPowerup.kind)
        self.powerupLogic.makePowerup(gameState, powerupType, diffPowerup.position, diffPowerup.id)

    def synchRemovedPowerup(self, gameState, diffPowerupId):
        powerup = Query(gameState.powerups).firstOrNone(lambda x: x.id == diffPowerupId)
        if powerup is not None:
            self.powerupLogic.removePowerup(gameState, powerup)
