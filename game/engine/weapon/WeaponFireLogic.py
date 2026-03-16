from game.engine.weapon.BulletLogic import BulletLogic
from game.engine.weapon.WeaponFeedbackLogic import WeaponFeedbackLogic
from game.engine.weapon.WeaponSelector import WeaponSelector


class WeaponFireLogic:

    def __init__(
        self,
        weaponFeedbackLogic: WeaponFeedbackLogic,
        bulletLogic: BulletLogic,
        weaponSelector: WeaponSelector,
    ):
        self.weaponFeedbackLogic = weaponFeedbackLogic
        self.bulletLogic = bulletLogic
        self.weaponSelector = weaponSelector

    def fireCurrentWeapon(self, gameState, person, personItems):
        weapon = personItems.currentWeapon
        self.fireWeapon(gameState, person, weapon, personItems)

    def fireWeapon(self, gameState, person, weapon, personItems):
        if self.canFire(person, weapon):
            weapon.isFiring = True
            weapon.bulletsCount -= 1
            weapon.delayRemain.set(weapon.delay)
            if weapon.needReload:
                weapon.reloadDelayRemain.set(weapon.reloadDelay)
            self.weaponFeedbackLogic.applyFeedback(weapon)
            self.bulletLogic.makeBullet(gameState, person, weapon)
            self.weaponSelector.selectNextWeaponIfCurrentEmpty(person, personItems)
            gameState.updateStatistic.firedWeapons.append((person, weapon))

    def canFire(self, person, weapon):
        return weapon.delayRemain.isExpired() and person.weaponSelectState is None and weapon.bulletsCount > 0

    def fireWeaponAltBullet(self, gameState, person, weapon, personItems):
        if self.canFireAltBullet(person, weapon):
            weapon.isFiring = True
            weapon.altBulletsCount -= 1
            weapon.delayRemain.set(weapon.delay)
            if weapon.needReload:
                weapon.reloadDelayRemain.set(weapon.reloadDelay)
            self.weaponFeedbackLogic.applyFeedback(weapon)
            self.bulletLogic.makeAltBullet(gameState, person, weapon)
            self.weaponSelector.selectNextWeaponIfCurrentEmpty(person, personItems)
            gameState.updateStatistic.firedWeapons.append((person, weapon))

    def canFireAltBullet(self, person, weapon):
        return weapon.delayRemain.isExpired() and person.weaponSelectState is None and weapon.altBulletsCount > 0
