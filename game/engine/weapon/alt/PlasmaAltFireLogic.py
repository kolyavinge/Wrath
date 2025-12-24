from game.engine.weapon.RayFireLogic import RayFireLogic
from game.model.person.PersonInputData import FireState


class PlasmaAltFireLogic:

    def __init__(self, rayFireLogic: RayFireLogic):
        self.rayFireLogic = rayFireLogic

    def apply(self, person, personItems, inputData):
        if inputData.altFireState == FireState.activated:
            self.rayFireLogic.activateRay(person, personItems.currentWeapon)
        elif inputData.altFireState == FireState.active:
            self.rayFireLogic.fire(person, personItems)
        elif inputData.altFireState == FireState.deactivated:
            self.rayFireLogic.deactivateRay(person, personItems.currentWeapon)
