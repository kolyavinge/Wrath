from game.engine.weapon.RayLogic import RayLogic
from game.model.person.PersonInputData import FireState


class PlasmaAltFireLogic:

    def __init__(self, rayLogic: RayLogic):
        self.rayLogic = rayLogic

    def apply(self, person, personItems, inputData):
        if inputData.altFireState == FireState.activated:
            self.rayLogic.makeRay(personItems.currentWeapon)
        elif inputData.altFireState == FireState.deactivated:
            self.rayLogic.removeRay(personItems.currentWeapon)
