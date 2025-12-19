from game.engine.GameData import GameData
from game.engine.weapon.WeaponFireLogic import WeaponFireLogic


class WeaponFireUpdater:

    def __init__(
        self,
        gameData: GameData,
        weaponFireLogic: WeaponFireLogic,
    ):
        self.gameData = gameData
        self.weaponFireLogic = weaponFireLogic

    def update(self):
        for person, inputData in self.gameData.allPersonInputData.items():
            personItems = self.gameData.allPersonItems[person]
            personItems.currentWeapon.isFiring = False
            if inputData.fire:
                self.weaponFireLogic.fire(person, personItems)
