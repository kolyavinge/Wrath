from game.engine.weapon.RayLogic import RayLogic
from game.engine.weapon.WeaponSelector import WeaponSelector
from game.lib.Query import Query


class RayFireLogic:

    def __init__(
        self,
        rayLogic: RayLogic,
        weaponSelector: WeaponSelector,
    ):
        self.rayLogic = rayLogic
        self.weaponSelector = weaponSelector

    def activateRay(self, gameState, person, weapon):
        if self.canFire(person, weapon):
            ray = self.rayLogic.makeRay(gameState, person, weapon)
            gameState.updateStatistic.activatedRays.append((person, weapon, ray))

    def fire(self, person, personItems):
        weapon = personItems.currentWeapon
        if self.canFire(person, weapon):
            weapon.isFiring = True
            if weapon.delayRemain.isExpired():
                weapon.bulletsCount -= 1
                weapon.delayRemain.set(weapon.delay)
                self.weaponSelector.selectNextWeaponIfCurrentEmpty(person, personItems)

    def canFire(self, person, weapon):
        return person.weaponSelectState is None and weapon.bulletsCount > 0

    def deactivateRay(self, gameState, person, weapon):
        ray = Query(gameState.rays).first(lambda r: r.weapon == weapon)
        self.rayLogic.removeRay(gameState, ray)
        weapon.delayRemain.set(2 * weapon.delay)
        gameState.updateStatistic.deactivatedRays.append((person, weapon, ray))
