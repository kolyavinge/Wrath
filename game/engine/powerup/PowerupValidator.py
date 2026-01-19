from game.anx.PersonConstants import PersonConstants
from game.model.powerup.LargeHealthPowerup import LargeHealthPowerup
from game.model.powerup.SmallHealthPowerup import SmallHealthPowerup
from game.model.powerup.VestPowerup import VestPowerup
from game.model.powerup.WeaponPowerup import WeaponPowerup


class PowerupValidator:

    def __init__(self):
        self.actions = {}
        self.actions[WeaponPowerup] = self.canApplyWeaponPowerup
        self.actions[LargeHealthPowerup] = self.canApplyHealthPowerup
        self.actions[SmallHealthPowerup] = self.canApplyHealthPowerup
        self.actions[VestPowerup] = self.canApplyVestPowerup

    def canApply(self, person, personItems, powerup):
        return self.actions[type(powerup)](person, personItems, powerup)

    def canApplyWeaponPowerup(self, person, personItems, powerup):
        findedWeapons = personItems.getWeaponsByType(powerup.weaponType)
        if len(findedWeapons) == 0:
            return True

        for findedWeapon in findedWeapons:
            if findedWeapon.bulletsCount < findedWeapon.maxBulletsCount:
                return True

        return False

    def canApplyHealthPowerup(self, person, personItems, powerup):
        return person.health < PersonConstants.maxPersonHealth

    def canApplyVestPowerup(self, person, personItems, powerup):
        return personItems.vest < PersonConstants.maxVest
