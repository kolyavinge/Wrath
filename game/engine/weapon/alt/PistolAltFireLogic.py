from game.engine.weapon.WeaponFireLogic import WeaponFireLogic
from game.model.person.PersonInputData import FireState


class PistolAltFireLogic:

    def __init__(self, weaponFireLogic: WeaponFireLogic):
        self.weaponFireLogic = weaponFireLogic

    def apply(self, person, personItems, inputData):
        if inputData.altFireState == FireState.activated or inputData.altFireState == FireState.active:
            self.weaponFireLogic.fireWeapon(person, personItems.leftHandWeapon, personItems)
            self.weaponFireLogic.fireWeapon(person, personItems.rightHandWeapon, personItems)
