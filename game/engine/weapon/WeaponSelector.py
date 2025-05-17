from game.anx.Events import Events
from game.engine.GameData import GameData
from game.engine.person.AimStateSwitcher import AimStateSwitcher
from game.lib.EventManager import EventManager
from game.model.weapon.NullWeapon import NullWeapon
from game.model.weapon.WeaponCollection import WeaponCollection


class WeaponSelector:

    def __init__(
        self,
        gameData: GameData,
        aimStateSwitcher: AimStateSwitcher,
        eventManager: EventManager,
    ):
        self.gameData = gameData
        self.aimStateSwitcher = aimStateSwitcher
        eventManager.attachToEvent(Events.selectWeaponRequested, self.onSelectWeaponRequested)

    def onSelectWeaponRequested(self, args):
        person, weaponNumber = args
        requestedWeaponType = WeaponCollection.getWeaponTypeByNumber(weaponNumber)
        self.selectWeaponByType(person, requestedWeaponType)

    def selectWeaponByType(self, person, weaponType):
        personItems = self.gameData.allPersonItems[person]
        if weaponType.defaultCount == 1:
            findedWeapon = personItems.getWeaponByTypeOrNone(weaponType)
            if findedWeapon is not None:
                self.setWeapons(person, personItems, findedWeapon, None, findedWeapon)
        elif weaponType.defaultCount == 2:
            findedWeapons = personItems.getWeaponsByType(weaponType)
            if len(findedWeapons) == 2:
                rightHandWeapon = findedWeapons[0]
                leftHandWeapon = findedWeapons[1]
                # в левом стволе может быть на одну пулю больше, если последний раз кол-во выстрелов было непарным
                currentWeapon = rightHandWeapon if rightHandWeapon.bulletsCount == leftHandWeapon.bulletsCount else leftHandWeapon
                self.setWeapons(person, personItems, rightHandWeapon, leftHandWeapon, currentWeapon)

    def selectNextWeapon(self, person, weapon):
        personItems = self.gameData.allPersonItems[person]
        if personItems.hasWeapons():
            weaponType = type(weapon)
            nextWeaponType = WeaponCollection.getNextWeaponTypeFor(weaponType)
            for _ in range(1, WeaponCollection.weaponTypesCount):
                if personItems.hasWeaponByType(nextWeaponType):
                    self.selectWeaponByType(person, nextWeaponType)
                    return
                else:
                    nextWeaponType = WeaponCollection.getNextWeaponTypeFor(nextWeaponType)
        else:
            self.setWeapons(person, personItems, NullWeapon.instance, None, NullWeapon.instance)

    def selectNextWeaponIfCurrentEmpty(self, person, personItems, weapon):
        if personItems.isCurrentWeaponEmpty():
            personItems.removeWeaponByType(type(weapon))
            self.selectNextWeapon(person, weapon)

    def setWeapons(self, person, personItems, rightHandWeapon, leftHandWeapon, currentWeapon):
        if person.isPlayer:
            self.aimStateSwitcher.setToDefaultIfNeeded()
        personItems.rightHandWeapon = rightHandWeapon
        personItems.leftHandWeapon = leftHandWeapon
        personItems.currentWeapon = currentWeapon
