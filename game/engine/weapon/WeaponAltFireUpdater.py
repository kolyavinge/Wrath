from game.engine.weapon.alt.LauncherAltFireLogic import LauncherAltFireLogic
from game.engine.weapon.alt.PistolAltFireLogic import PistolAltFireLogic
from game.engine.weapon.alt.PlasmaAltFireLogic import PlasmaAltFireLogic
from game.engine.weapon.alt.RailgunAltFireLogic import RailgunAltFireLogic
from game.engine.weapon.alt.RifleAltFireLogic import RifleAltFireLogic
from game.engine.weapon.alt.SniperAltFireLogic import SniperAltFireLogic
from game.engine.weapon.WeaponAltFireStateSwitcher import WeaponAltFireStateSwitcher
from game.model.weapon.Launcher import Launcher
from game.model.weapon.Pistol import Pistol
from game.model.weapon.Plasma import Plasma
from game.model.weapon.Railgun import Railgun
from game.model.weapon.Rifle import Rifle
from game.model.weapon.Sniper import Sniper
from game.model.weapon.Weapon import FireState


class WeaponAltFireUpdater:

    def __init__(
        self,
        pistolAltFireLogic: PistolAltFireLogic,
        rifleAltFireLogic: RifleAltFireLogic,
        plasmaAltFireLogic: PlasmaAltFireLogic,
        launcherAltFireLogic: LauncherAltFireLogic,
        railgunAltFireLogic: RailgunAltFireLogic,
        sniperAltFireLogic: SniperAltFireLogic,
        weaponAltFireStateSwitcher: WeaponAltFireStateSwitcher,
    ):
        self.altFireLogic = {}
        self.altFireLogic[Pistol] = pistolAltFireLogic
        self.altFireLogic[Rifle] = rifleAltFireLogic
        self.altFireLogic[Plasma] = plasmaAltFireLogic
        self.altFireLogic[Launcher] = launcherAltFireLogic
        self.altFireLogic[Railgun] = railgunAltFireLogic
        self.altFireLogic[Sniper] = sniperAltFireLogic
        self.weaponAltFireStateSwitcher = weaponAltFireStateSwitcher

    def updateForPlayer(self, gameState):
        self.updateForPerson(gameState, gameState.player, gameState.playerInputData)

    def updateForBots(self, gameState):
        for bot, inputData in gameState.botInputData.items():
            self.updateForPerson(gameState, bot, inputData)

    def updateForPerson(self, gameState, person, inputData):
        personItems = gameState.allPersonItems[person]
        weapon = personItems.currentWeapon
        weaponType = type(weapon)
        if inputData.fire and not weapon.allowFireWithAltFire:
            self.deactivateAltFire(gameState, person, personItems, weaponType, weapon)
        elif person.weaponSelectState is not None:
            self.deactivateAltFire(gameState, person, personItems, weaponType, weapon)
        else:
            self.applyAltFire(gameState, person, personItems, weaponType, weapon, inputData)

    def applyAltFire(self, gameState, person, personItems, weaponType, weapon, inputData):
        self.weaponAltFireStateSwitcher.switch(weapon, inputData.altFire)
        if weapon.altFireState != FireState.deactive:
            self.altFireLogic[weaponType].apply(gameState, person, personItems, weapon)

    def deactivateAltFire(self, gameState, person, personItems, weaponType, weapon):
        if weapon.altFireState != FireState.deactive:
            weapon.altFireState = FireState.deactivated
            self.altFireLogic[weaponType].apply(gameState, person, personItems, weapon)
            weapon.altFireState = FireState.deactive
