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
        self.rightHandWeapon = pistol1
        self.leftHandWeapon = pistol2
        self.currentWeapon = self.rightHandWeapon
        self.vest = 0

    def setFullVest(self):
        self.vest = PersonConstants.maxVest

    def damageVest(self, value):
        if value < 0:
            raise Exception("value cannot be negative.")

        self.vest = int(Math.max(self.vest - value, 0))

    def setWeaponByType(self, weaponType):
        self.rightHandWeapon = Query(self.weapons).first(lambda x: type(x) == weaponType)
        self.currentWeapon = self.rightHandWeapon
        if self.rightHandWeapon.defaultCount == 1:
            self.leftHandWeapon = None
        elif self.rightHandWeapon.defaultCount == 2:
            self.leftHandWeapon = Query(self.weapons).first(lambda x: type(x) == weaponType and x != self.rightHandWeapon)
            assert self.leftHandWeapon != self.rightHandWeapon
