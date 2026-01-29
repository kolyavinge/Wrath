from game.engine.person.PersonTurnLogic import PersonTurnLogic
from game.engine.person.PersonWeaponPositionUpdater import PersonWeaponPositionUpdater
from game.engine.powerup.PowerupLogic import PowerupLogic
from game.engine.weapon.BulletLogic import BulletLogic
from game.engine.weapon.BulletPositionUpdater import BulletPositionUpdater
from game.engine.weapon.WeaponSelector import WeaponSelector
from game.lib.Query import Query
from game.model.powerup.PowerupType import PowerupType
from game.model.weapon.WeaponCollection import WeaponCollection


class GameStateSynchronizer:

    def __init__(
        self,
        personTurnLogic: PersonTurnLogic,
        bulletLogic: BulletLogic,
        bulletPositionUpdater: BulletPositionUpdater,
        weaponSelector: WeaponSelector,
        personWeaponPositionUpdater: PersonWeaponPositionUpdater,
        powerupLogic: PowerupLogic,
    ):
        self.personTurnLogic = personTurnLogic
        self.bulletLogic = bulletLogic
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

    def synchAddedPowerup(self, gameState, diffPowerup):
        powerupType = PowerupType.getPowerupTypeFromKind(diffPowerup.kind)
        self.powerupLogic.makePowerup(gameState, powerupType, diffPowerup.position, diffPowerup.id)

    def synchRemovedPowerup(self, gameState, diffPowerupId):
        powerup = Query(gameState.powerups).firstOrNone(lambda x: x.id == diffPowerupId)
        if powerup is not None:
            self.powerupLogic.removePowerup(gameState, powerup)
