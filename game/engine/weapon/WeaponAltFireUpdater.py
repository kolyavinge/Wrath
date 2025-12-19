from game.engine.GameData import GameData
from game.engine.weapon.LauncherAltFireLogic import LauncherAltFireLogic
from game.engine.weapon.RailgunAltFireLogic import RailgunAltFireLogic
from game.engine.weapon.SniperAltFireLogic import SniperAltFireLogic
from game.model.person.PersonInputData import FireState
from game.model.weapon.Launcher import Launcher
from game.model.weapon.Railgun import Railgun
from game.model.weapon.Sniper import Sniper


class WeaponAltFireUpdater:

    def __init__(
        self,
        gameData: GameData,
        launcherAltFireLogic: LauncherAltFireLogic,
        railgunAltFireLogic: RailgunAltFireLogic,
        sniperAltFireLogic: SniperAltFireLogic,
    ):
        self.gameData = gameData
        self.altFireLogic = {}
        self.altFireLogic[Launcher] = launcherAltFireLogic
        self.altFireLogic[Railgun] = railgunAltFireLogic
        self.altFireLogic[Sniper] = sniperAltFireLogic

    def update(self):
        for person, inputData in self.gameData.allPersonInputData.items():
            if not inputData.fire and inputData.altFireState != FireState.deactive:
                personItems = self.gameData.allPersonItems[person]
                weaponType = personItems.getCurrentWeaponType()
                if weaponType in self.altFireLogic:
                    self.altFireLogic[weaponType].apply(person, personItems, inputData)
