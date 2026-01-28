from game.engine.person.PersonTurnLogic import PersonTurnLogic
from game.engine.person.PersonWeaponPositionUpdater import PersonWeaponPositionUpdater
from game.engine.weapon.BulletLogic import BulletLogic
from game.engine.weapon.BulletPositionUpdater import BulletPositionUpdater
from game.engine.weapon.WeaponSelector import WeaponSelector
from game.model.weapon.WeaponCollection import WeaponCollection


class GameStateSynchronizer:

    def __init__(
        self,
        personTurnLogic: PersonTurnLogic,
        bulletLogic: BulletLogic,
        bulletPositionUpdater: BulletPositionUpdater,
        weaponSelector: WeaponSelector,
        personWeaponPositionUpdater: PersonWeaponPositionUpdater,
    ):
        self.personTurnLogic = personTurnLogic
        self.bulletLogic = bulletLogic
        self.bulletPositionUpdater = bulletPositionUpdater
        self.weaponSelector = weaponSelector
        self.personWeaponPositionUpdater = personWeaponPositionUpdater

    def applySnapshotDiff(self, gameState, diff):
        if hasattr(diff, "player"):
            self.synchPerson(gameState, diff.player)

        if hasattr(diff, "enemies"):
            for enemy in diff.enemies:
                self.synchPerson(gameState, enemy)

        if hasattr(diff, "bullets"):
            for bullet in diff.bullets:
                self.synchBullet(gameState, bullet)

    def synchPerson(self, gameState, diffPerson):
        sychedPerson = gameState.allPersonById[diffPerson.id]
        sychedPerson.moveNextPositionTo(diffPerson.centerPoint)
        self.personTurnLogic.setYawPitchRadians(sychedPerson, diffPerson.yawRadians, diffPerson.pitchRadians)
        sychedPerson.commitNextPosition()

    def synchBullet(self, gameState, diffBullet):
        if diffBullet.id not in gameState.bulletsById:
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
