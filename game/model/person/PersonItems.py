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
        self.rightHandWeapon = plasma
        self.leftHandWeapon = None
        self.currentWeapon = self.rightHandWeapon
        self.vest = 0

    def setFullVest(self):
        self.vest = 100
