from game.engine.weapon.GrenadeFireLogic import GrenadeFireLogic
from game.model.weapon.Weapon import FireState


class RifleAltFireLogic:

    def __init__(
        self,
        grenadeFireLogic: GrenadeFireLogic,
    ):
        self.grenadeFireLogic = grenadeFireLogic

    def apply(self, gameState, person, personItems, weapon):
        if weapon.altFireState == FireState.activated or weapon.altFireState == FireState.active:
            self.grenadeFireLogic.fireWeapon(gameState, person, personItems, weapon)
