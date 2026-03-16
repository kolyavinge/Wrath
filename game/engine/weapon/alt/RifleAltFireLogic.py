from game.engine.weapon.WeaponFireLogic import WeaponFireLogic
from game.model.weapon.Weapon import FireState


class RifleAltFireLogic:

    def __init__(
        self,
        weaponFireLogic: WeaponFireLogic,
    ):
        self.weaponFireLogic = weaponFireLogic

    def apply(self, gameState, person, personItems, weapon):
        if weapon.altFireState == FireState.activated or weapon.altFireState == FireState.active:
            self.weaponFireLogic.fireWeaponAltBullet(gameState, person, weapon, personItems)
