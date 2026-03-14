from game.engine.weapon.GrenadeLogic import GrenadeLogic
from game.engine.weapon.WeaponFeedbackLogic import WeaponFeedbackLogic
from game.engine.weapon.WeaponSelector import WeaponSelector


class GrenadeFireLogic:

    def __init__(
        self,
        weaponFeedbackLogic: WeaponFeedbackLogic,
        grenadeLogic: GrenadeLogic,
        weaponSelector: WeaponSelector,
    ):
        self.weaponFeedbackLogic = weaponFeedbackLogic
        self.grenadeLogic = grenadeLogic
        self.weaponSelector = weaponSelector

    def fireWeapon(self, gameState, person, personItems, weapon):
        if self.canFire(person, weapon):
            weapon.isFiring = True
            weapon.grenadesCount -= 1
            weapon.delayRemain.set(weapon.delay)
            self.weaponFeedbackLogic.applyFeedback(weapon)
            self.grenadeLogic.makeGrenade(gameState, person, weapon)
            self.weaponSelector.selectNextWeaponIfCurrentEmpty(person, personItems)
            gameState.updateStatistic.firedWeapons.append((person, weapon))

    def canFire(self, person, weapon):
        return weapon.delayRemain.isExpired() and person.weaponSelectState is None and weapon.grenadesCount > 0
