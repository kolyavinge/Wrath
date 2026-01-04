from game.engine.GameState import GameState
from game.engine.weapon.WeaponFireLogic import WeaponFireLogic


class WeaponFireUpdater:

    def __init__(
        self,
        gameData: GameState,
        weaponFireLogic: WeaponFireLogic,
    ):
        self.gameData = gameData
        self.weaponFireLogic = weaponFireLogic

    def update(self):
        for person, inputData in self.gameData.allPersonInputData.items():
            personItems = self.gameData.allPersonItems[person]

            # reset firing before process fire
            personItems.rightHandWeapon.isFiring = False
            if personItems.leftHandWeapon is not None:
                personItems.leftHandWeapon.isFiring = False

            if inputData.fire and (not inputData.altFire or personItems.currentWeapon.allowFireWithAltFire):
                self.weaponFireLogic.fireCurrentWeapon(person, personItems)
