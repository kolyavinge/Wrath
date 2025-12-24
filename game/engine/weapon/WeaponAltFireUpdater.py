from game.engine.GameData import GameData
from game.engine.weapon.alt.LauncherAltFireLogic import LauncherAltFireLogic
from game.engine.weapon.alt.PistolAltFireLogic import PistolAltFireLogic
from game.engine.weapon.alt.PlasmaAltFireLogic import PlasmaAltFireLogic
from game.engine.weapon.alt.RailgunAltFireLogic import RailgunAltFireLogic
from game.engine.weapon.alt.SniperAltFireLogic import SniperAltFireLogic
from game.model.person.PersonInputData import FireState
from game.model.weapon.Launcher import Launcher
from game.model.weapon.Pistol import Pistol
from game.model.weapon.Plasma import Plasma
from game.model.weapon.Railgun import Railgun
from game.model.weapon.Sniper import Sniper


class WeaponAltFireUpdater:

    def __init__(
        self,
        gameData: GameData,
        pistolAltFireLogic: PistolAltFireLogic,
        plasmaAltFireLogic: PlasmaAltFireLogic,
        launcherAltFireLogic: LauncherAltFireLogic,
        railgunAltFireLogic: RailgunAltFireLogic,
        sniperAltFireLogic: SniperAltFireLogic,
    ):
        self.gameData = gameData
        self.altFireLogic = {}
        self.altFireLogic[Pistol] = pistolAltFireLogic
        self.altFireLogic[Plasma] = plasmaAltFireLogic
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
