from game.anx.PersonConstants import PersonConstants
from game.lib.Math import Math
from game.lib.Query import Query
from game.model.weapon.Launcher import Launcher
from game.model.weapon.Pistol import Pistol
from game.model.weapon.Plasma import Plasma
from game.model.weapon.Railgun import Railgun
from game.model.weapon.Rifle import Rifle
from game.model.weapon.Sniper import Sniper


class PersonItems:

    def __init__(self):
        pistol1 = Pistol()
        pistol2 = Pistol()
        rifle = Rifle()
        plasma = Plasma()
        launcher = Launcher()
        railgun = Railgun()
        sniper = Sniper()

        self.weapons = set()
        self.weapons.add(pistol1)
        self.weapons.add(pistol2)
        self.weapons.add(rifle)
        self.weapons.add(plasma)
        self.weapons.add(launcher)
        self.weapons.add(railgun)
        self.weapons.add(sniper)
        self.rightHandWeapon = None
        self.leftHandWeapon = None
        self.currentWeapon = None
        self.vest = 0

    def setFullVest(self):
        self.vest = PersonConstants.maxVest

    def damageVest(self, value):
        if value < 0:
            raise Exception("value cannot be negative.")

        self.vest = int(Math.max(self.vest - value, 0))

    def hasWeaponByType(self, weaponType):
        return Query(self.weapons).any(lambda x: type(x) == weaponType)

    def removeWeaponByType(self, weaponType):
        weapons = Query(self.weapons).where(lambda x: type(x) == weaponType).result
        for weapon in weapons:
            self.weapons.remove(weapon)
