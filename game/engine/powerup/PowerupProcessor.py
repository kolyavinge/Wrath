from game.engine.GameState import GameState
from game.engine.weapon.WeaponSelector import WeaponSelector
from game.model.powerup.LargeHealthPowerup import LargeHealthPowerup
from game.model.powerup.SmallHealthPowerup import SmallHealthPowerup
from game.model.powerup.VestPowerup import VestPowerup
from game.model.powerup.WeaponPowerup import WeaponPowerup


class PowerupProcessor:

    def __init__(
        self,
        gameData: GameState,
        weaponSelector: WeaponSelector,
    ):
        self.gameData = gameData
        self.weaponSelector = weaponSelector
        self.actions = {}
        self.actions[WeaponPowerup] = self.applyWeaponPowerup
        self.actions[LargeHealthPowerup] = self.applyHealthPowerup
        self.actions[SmallHealthPowerup] = self.applyHealthPowerup
        self.actions[VestPowerup] = self.applyVestPowerup

    def apply(self, person, powerup):
        self.actions[type(powerup)](person, powerup)

    def applyWeaponPowerup(self, person, powerup):
        personItems = self.gameData.allPersonItems[person]
        findedWeapons = personItems.getWeaponsByType(powerup.weaponType)
        if len(findedWeapons) > 0:
            for findedWeapon in findedWeapons:
                findedWeapon.addBullets(findedWeapon.maxBulletsCount)
        else:
            selectThisWeapon = not personItems.hasWeapons()
            for _ in range(0, powerup.count):
                personItems.weapons.add(powerup.weaponType())
            if selectThisWeapon:
                self.weaponSelector.selectWeaponByType(person, powerup.weaponType)

    def applyHealthPowerup(self, person, powerup):
        person.addHealth(powerup.value)

    def applyVestPowerup(self, person, powerup):
        self.gameData.allPersonItems[person].setFullVest()
