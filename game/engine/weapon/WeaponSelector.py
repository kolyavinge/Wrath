from game.anx.PersonConstants import PersonConstants
from game.engine.GameData import GameData
from game.engine.person.AimStateSwitcher import AimStateSwitcher
from game.model.person.Player import Player
from game.model.weapon.NullWeapon import NullWeapon
from game.model.weapon.WeaponCollection import WeaponCollection


class WeaponSelector:

    def __init__(
        self,
        gameData: GameData,
        aimStateSwitcher: AimStateSwitcher,
    ):
        self.gameData = gameData
        self.aimStateSwitcher = aimStateSwitcher

    def initWeaponByType(self, person, weaponType):
        personItems = self.gameData.allPersonItems[person]
        if weaponType.defaultCount == 1:
            findedWeapon = personItems.getWeaponByTypeOrNone(weaponType)
            assert findedWeapon is not None
            personItems.rightHandWeapon = findedWeapon
            personItems.leftHandWeapon = None
            personItems.currentWeapon = findedWeapon
        elif weaponType.defaultCount == 2:
            findedWeapons = personItems.getWeaponsByType(weaponType)
            assert len(findedWeapons) == 2
            rightHandWeapon = findedWeapons[0]
            leftHandWeapon = findedWeapons[1]
            currentWeapon = rightHandWeapon
            personItems.rightHandWeapon = rightHandWeapon
            personItems.leftHandWeapon = leftHandWeapon
            personItems.currentWeapon = currentWeapon

    def selectWeaponByType(self, person, weaponType):
        personItems = self.gameData.allPersonItems[person]
        if weaponType.defaultCount == 1:
            findedWeapon = personItems.getWeaponByTypeOrNone(weaponType)
            if findedWeapon is not None:
                self.selectWeapons(person, personItems, findedWeapon, None, findedWeapon)
        elif weaponType.defaultCount == 2:
            findedWeapons = personItems.getWeaponsByType(weaponType)
            if len(findedWeapons) == 2:
                rightHandWeapon = findedWeapons[0]
                leftHandWeapon = findedWeapons[1]
                # в левом стволе может быть на одну пулю больше, если последний раз кол-во выстрелов было непарным
                currentWeapon = rightHandWeapon if rightHandWeapon.bulletsCount == leftHandWeapon.bulletsCount else leftHandWeapon
                self.selectWeapons(person, personItems, rightHandWeapon, leftHandWeapon, currentWeapon)

    def selectNextWeapon(self, person):
        personItems = self.gameData.allPersonItems[person]
        if personItems.hasWeapons():
            weaponType = personItems.getCurrentWeaponType()
            nextWeaponType = WeaponCollection.getNextWeaponTypeFor(weaponType)
            for _ in range(1, WeaponCollection.weaponTypesCount):
                if personItems.hasWeaponByType(nextWeaponType):
                    self.selectWeaponByType(person, nextWeaponType)
                    return
                else:
                    nextWeaponType = WeaponCollection.getNextWeaponTypeFor(nextWeaponType)
        else:
            self.selectWeapons(person, personItems, NullWeapon.instance, None, NullWeapon.instance)

    def selectPrevWeapon(self, person):
        personItems = self.gameData.allPersonItems[person]
        if personItems.hasWeapons():
            weaponType = personItems.getCurrentWeaponType()
            prevWeaponType = WeaponCollection.getPrevWeaponTypeFor(weaponType)
            for _ in range(1, WeaponCollection.weaponTypesCount):
                if personItems.hasWeaponByType(prevWeaponType):
                    self.selectWeaponByType(person, prevWeaponType)
                    return
                else:
                    prevWeaponType = WeaponCollection.getPrevWeaponTypeFor(prevWeaponType)
        else:
            self.selectWeapons(person, personItems, NullWeapon.instance, None, NullWeapon.instance)

    def selectNextWeaponIfCurrentEmpty(self, person, personItems):
        if personItems.isCurrentWeaponEmpty():
            personItems.removeWeaponByType(personItems.getCurrentWeaponType())
            self.selectNextWeapon(person)

    def selectWeapons(self, person, personItems, rightHandWeapon, leftHandWeapon, currentWeapon):
        if personItems.currentWeapon == currentWeapon:
            return
        if type(person) == Player:
            self.aimStateSwitcher.setToDefaultIfNeeded()
        personItems.selectedRightHandWeapon = rightHandWeapon
        personItems.selectedLeftHandWeapon = leftHandWeapon
        personItems.selectedCurrentWeapon = currentWeapon
        # при быстром переключении оружия задержка все равно активируется один раз
        if person.selectWeaponDelay.isExpired():
            person.selectWeaponDelay.set(PersonConstants.selectWeaponDelay)
