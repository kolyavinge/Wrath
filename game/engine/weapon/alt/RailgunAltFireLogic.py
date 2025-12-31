from game.engine.weapon.WeaponFireLogic import WeaponFireLogic
from game.model.weapon.Weapon import FireState


class RailgunAltFireLogic:

    def __init__(self, weaponFireLogic: WeaponFireLogic):
        self.weaponFireLogic = weaponFireLogic

    def apply(self, person, personItems, weapon):
        if weapon.altFireState == FireState.activated:
            if weapon.delayRemain.isExpired():
                weapon.chargeDelay.reset()
                weapon.altFireLimitDelay.reset()
            else:
                weapon.altFireState = FireState.deactive
        elif weapon.altFireState == FireState.active:
            weapon.chargeDelay.decrease()
            weapon.altFireLimitDelay.decrease()
            if weapon.altFireLimitDelay.isExpired():
                self.fire(person, personItems, weapon)
                weapon.altFireState = FireState.deactive
        elif weapon.altFireState == FireState.deactivated:
            self.fire(person, personItems, weapon)

    def fire(self, person, personItems, weapon):
        weapon.isCharged = weapon.chargeDelay.isExpired()
        self.weaponFireLogic.fireCurrentWeapon(person, personItems)
        weapon.chargeDelay.reset()
        weapon.altFireLimitDelay.reset()
