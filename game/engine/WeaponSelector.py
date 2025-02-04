from game.anx.Events import Events
from game.engine.AimStateSwitcher import AimStateSwitcher
from game.engine.GameData import GameData
from game.lib.EventManager import EventManager
from game.lib.Query import Query
from game.model.weapon.Launcher import Launcher
from game.model.weapon.Pistol import Pistol
from game.model.weapon.Plasma import Plasma
from game.model.weapon.Railgun import Railgun
from game.model.weapon.Rifle import Rifle
from game.model.weapon.Sniper import Sniper


class WeaponSelector:

    def __init__(self, gameData, aimStateSwitcher, eventManager):
        self.gameData = gameData
        self.aimStateSwitcher = aimStateSwitcher
        self.weapons = {}
        self.weapons[1] = Pistol
        self.weapons[2] = Rifle
        self.weapons[3] = Plasma
        self.weapons[4] = Launcher
        self.weapons[5] = Railgun
        self.weapons[6] = Sniper
        eventManager.attachToEvent(Events.selectWeaponRequested, self.selectWeapon)

    def selectWeapon(self, weaponNumber):
        self.aimStateSwitcher.setToDefaultIfNeeded()
        requestedWeaponType = self.weapons[weaponNumber]
        playerItems = self.gameData.playerItems
        if requestedWeaponType.defaultCount == 1:
            findedWeapon = Query(playerItems.weapons).firstOrNone(lambda x: type(x) == requestedWeaponType)
            if findedWeapon is not None:
                playerItems.rightHandWeapon = findedWeapon
                playerItems.leftHandWeapon = None
                playerItems.currentWeapon = playerItems.rightHandWeapon
        elif requestedWeaponType.defaultCount == 2:
            findedWeapons = Query(playerItems.weapons).where(lambda x: type(x) == requestedWeaponType).result
            if len(findedWeapons) == 2:
                playerItems.rightHandWeapon = findedWeapons[0]
                playerItems.leftHandWeapon = findedWeapons[1]
                playerItems.currentWeapon = playerItems.rightHandWeapon


def makeWeaponSelector(resolver):
    return WeaponSelector(resolver.resolve(GameData), resolver.resolve(AimStateSwitcher), resolver.resolve(EventManager))
