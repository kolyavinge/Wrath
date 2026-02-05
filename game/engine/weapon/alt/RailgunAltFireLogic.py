from game.engine.weapon.WeaponFireLogic import WeaponFireLogic
from game.model.weapon.Weapon import FireState


class RailgunAltFireLogic:

    def __init__(
        self,
        weaponFireLogic: WeaponFireLogic,
    ):
        self.weaponFireLogic = weaponFireLogic

    def apply(self, gameState, person, personItems, weapon):
        if weapon.altFireState == FireState.activated:
            if weapon.delayRemain.isExpired():
                weapon.chargeDelay.reset()
                weapon.altFireLimitDelay.reset()
                gameState.updateStatistic.activatedRailgunCharging.append((person, weapon))
            else:
                weapon.altFireState = FireState.deactive
        elif weapon.altFireState == FireState.active:
            weapon.chargeDelay.decrease()
            weapon.altFireLimitDelay.decrease()
            if weapon.altFireLimitDelay.isExpired():
                self.fire(gameState, person, personItems, weapon)
                weapon.altFireState = FireState.deactive
        elif weapon.altFireState == FireState.deactivated:
            self.fire(gameState, person, personItems, weapon)

    def fire(self, gameState, person, personItems, weapon):
        weapon.isCharged = weapon.chargeDelay.isExpired()
        self.weaponFireLogic.fireCurrentWeapon(gameState, person, personItems)
        weapon.chargeDelay.reset()
        weapon.altFireLimitDelay.reset()
        gameState.updateStatistic.deactivatedRailgunCharging.append((person, weapon))
