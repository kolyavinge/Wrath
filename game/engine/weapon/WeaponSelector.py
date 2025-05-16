from game.anx.Events import Events
from game.engine.GameData import GameData
from game.engine.person.AimStateSwitcher import AimStateSwitcher
from game.lib.EventManager import EventManager
from game.lib.Query import Query
from game.model.weapon.Launcher import Launcher
from game.model.weapon.Pistol import Pistol
from game.model.weapon.Plasma import Plasma
from game.model.weapon.Railgun import Railgun
from game.model.weapon.Rifle import Rifle
from game.model.weapon.Sniper import Sniper


class WeaponSelector:

    def __init__(
        self,
        gameData: GameData,
        aimStateSwitcher: AimStateSwitcher,
        eventManager: EventManager,
    ):
        self.gameData = gameData
        self.aimStateSwitcher = aimStateSwitcher

        self.weaponNumbers = {}
        self.weaponNumbers[1] = Pistol
        self.weaponNumbers[2] = Rifle
        self.weaponNumbers[3] = Plasma
        self.weaponNumbers[4] = Launcher
        self.weaponNumbers[5] = Railgun
        self.weaponNumbers[6] = Sniper

        eventManager.attachToEvent(Events.selectWeaponRequested, self.onSelectWeaponRequested)

    def onSelectWeaponRequested(self, args):
        person, weaponNumber = args
        requestedWeaponType = self.weaponNumbers[weaponNumber]
        self.selectWeaponByType(person, requestedWeaponType)

    def selectWeaponByType(self, person, weaponType):
        if person.isPlayer:
            self.aimStateSwitcher.setToDefaultIfNeeded()
        personItems = self.gameData.allPersonItems[person]
        if weaponType.defaultCount == 1:
            findedWeapon = Query(personItems.weapons).firstOrNone(lambda x: type(x) == weaponType)
            if findedWeapon is not None:
                personItems.rightHandWeapon = findedWeapon
                personItems.leftHandWeapon = None
                personItems.currentWeapon = personItems.rightHandWeapon
        elif weaponType.defaultCount == 2:
            findedWeapons = Query(personItems.weapons).where(lambda x: type(x) == weaponType).result
            if len(findedWeapons) == 2:
                personItems.rightHandWeapon = findedWeapons[0]
                personItems.leftHandWeapon = findedWeapons[1]
                # в левом стволе может быть на одну пулю больше, если последний раз кол-во выстрелов было непарным
                personItems.currentWeapon = (
                    personItems.rightHandWeapon
                    if personItems.rightHandWeapon.bulletsCount == personItems.leftHandWeapon.bulletsCount
                    else personItems.leftHandWeapon
                )
