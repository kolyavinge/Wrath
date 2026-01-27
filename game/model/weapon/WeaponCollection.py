from game.model.weapon.Launcher import Launcher
from game.model.weapon.Pistol import Pistol
from game.model.weapon.Plasma import Plasma
from game.model.weapon.Railgun import Railgun
from game.model.weapon.Rifle import Rifle
from game.model.weapon.Sniper import Sniper


class WeaponCollection:

    allWeaponTypes = [Pistol, Rifle, Plasma, Launcher, Railgun, Sniper]
    weaponTypesCount = len(allWeaponTypes)

    weaponByNumbers = {}
    weaponByNumbers[1] = Pistol
    weaponByNumbers[2] = Rifle
    weaponByNumbers[3] = Plasma
    weaponByNumbers[4] = Launcher
    weaponByNumbers[5] = Railgun
    weaponByNumbers[6] = Sniper

    weaponByTypes = {value: key for key, value in weaponByNumbers.items()}

    nextWeapons = {}
    nextWeapons[Pistol] = Rifle
    nextWeapons[Rifle] = Plasma
    nextWeapons[Plasma] = Launcher
    nextWeapons[Launcher] = Railgun
    nextWeapons[Railgun] = Sniper
    nextWeapons[Sniper] = Pistol

    prevWeapons = {}
    prevWeapons[Pistol] = Sniper
    prevWeapons[Rifle] = Pistol
    prevWeapons[Plasma] = Rifle
    prevWeapons[Launcher] = Plasma
    prevWeapons[Railgun] = Launcher
    prevWeapons[Sniper] = Railgun

    @staticmethod
    def getWeaponTypeByNumber(number):
        return WeaponCollection.weaponByNumbers[number]

    @staticmethod
    def getWeaponNumberByType(type):
        return WeaponCollection.weaponByTypes[type]

    @staticmethod
    def getNextWeaponTypeFor(weapon):
        return WeaponCollection.nextWeapons[weapon]

    @staticmethod
    def getPrevWeaponTypeFor(weapon):
        return WeaponCollection.prevWeapons[weapon]
