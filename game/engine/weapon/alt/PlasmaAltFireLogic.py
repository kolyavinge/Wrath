from game.engine.weapon.RayFireLogic import RayFireLogic
from game.model.weapon.Weapon import FireState


class PlasmaAltFireLogic:

    def __init__(self, rayFireLogic: RayFireLogic):
        self.rayFireLogic = rayFireLogic

    def apply(self, person, personItems, weapon):
        if weapon.altFireState == FireState.activated:
            self.rayFireLogic.activateRay(person, weapon)
        elif weapon.altFireState == FireState.active:
            self.rayFireLogic.fire(person, personItems)
        elif weapon.altFireState == FireState.deactivated:
            self.rayFireLogic.deactivateRay(person, weapon)
