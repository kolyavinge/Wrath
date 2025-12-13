from game.engine.weapon.BulletLogic import BulletLogic
from game.engine.weapon.WeaponFeedbackLogic import WeaponFeedbackLogic
from game.engine.weapon.WeaponSelector import WeaponSelector
from game.lib.EventManager import EventManager, Events


class WeaponFireLogic:

    def __init__(
        self,
        weaponFeedbackLogic: WeaponFeedbackLogic,
        bulletLogic: BulletLogic,
        weaponSelector: WeaponSelector,
        eventManager: EventManager,
    ):
        self.weaponFeedbackLogic = weaponFeedbackLogic
        self.bulletLogic = bulletLogic
        self.weaponSelector = weaponSelector
        self.eventManager = eventManager

    def fire(self, person, personItems):
        weapon = personItems.currentWeapon
        if self.canFire(person, weapon):
            weapon.isFiring = True
            weapon.bulletsCount -= 1
            weapon.delayRemain.set(weapon.delay)
            if weapon.needReload:
                weapon.reloadDelayRemain.set(weapon.reloadDelay)
            self.weaponFeedbackLogic.applyFeedback(weapon)
            self.bulletLogic.makeBullet(person, weapon)
            self.weaponSelector.selectNextWeaponIfCurrentEmpty(person, personItems)
            self.eventManager.raiseEvent(Events.weaponFired, (person, weapon))
        else:
            weapon.isFiring = False

    def canFire(self, person, weapon):
        return weapon.delayRemain.isExpired() and person.weaponSelectState is None and weapon.bulletsCount > 0
