from game.engine.weapon.WeaponFireLogic import WeaponFireLogic
from game.model.person.PersonInputData import FireState


class RailgunAltFireLogic:

    def __init__(self, weaponFireLogic: WeaponFireLogic):
        self.weaponFireLogic = weaponFireLogic

    def apply(self, person, personItems, inputData):
        weapon = personItems.currentWeapon
        if inputData.altFireState == FireState.activated:
            weapon.chargeDelay.reset()
        elif inputData.altFireState == FireState.active:
            weapon.chargeDelay.decrease()
        elif inputData.altFireState == FireState.deactivated:
            weapon.isCharged = weapon.chargeDelay.isExpired()
            self.weaponFireLogic.fireCurrentWeapon(person, personItems)
            weapon.chargeDelay.reset()
