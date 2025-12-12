from game.engine.GameData import GameData
from game.engine.weapon.LauncherAltFireLogic import LauncherAltFireLogic
from game.engine.weapon.SniperAltFireLogic import SniperAltFireLogic
from game.model.weapon.Launcher import Launcher
from game.model.weapon.Sniper import Sniper


class WeaponAltFireUpdater:

    def __init__(
        self,
        gameData: GameData,
        launcherAltFireLogic: LauncherAltFireLogic,
        sniperAltFireLogic: SniperAltFireLogic,
    ):
        self.gameData = gameData
        self.altFireLogic = {}
        self.altFireLogic[Launcher] = launcherAltFireLogic
        self.altFireLogic[Sniper] = sniperAltFireLogic

    def update(self):
        for person, inputData in self.gameData.allPersonInputData.items():
            personItems = self.gameData.allPersonItems[person]
            weaponType = personItems.getCurrentWeaponType()
            if weaponType in self.altFireLogic:
                self.altFireLogic[weaponType].apply(person, personItems.currentWeapon, inputData)
