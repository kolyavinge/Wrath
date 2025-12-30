from game.engine.weapon.WeaponFireLogic import WeaponFireLogic
from game.model.weapon.Weapon import FireState


class RailgunAltFireLogic:

    def __init__(self, weaponFireLogic: WeaponFireLogic):
        self.weaponFireLogic = weaponFireLogic

    def apply(self, person, personItems, weapon):
        if weapon.altFireState == FireState.activated:
            weapon.chargeDelay.reset()
        elif weapon.altFireState == FireState.active:
            weapon.chargeDelay.decrease()
        elif weapon.altFireState == FireState.deactivated:
            weapon.isCharged = weapon.chargeDelay.isExpired()
            self.weaponFireLogic.fireCurrentWeapon(person, personItems)
            weapon.chargeDelay.reset()
