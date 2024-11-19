from game.model.weapon.Launcher import Launcher
from game.model.weapon.Pistol import Pistol
from game.model.weapon.Plasma import Plasma
from game.model.weapon.Railgun import Railgun
from game.model.weapon.Rifle import Rifle
from game.model.weapon.Sniper import Sniper


class PersonItems:

    def __init__(self):
        self.rightHandWeapon = Sniper()
        self.leftHandWeapon = None
        self.currentWeapon = self.rightHandWeapon
        self.weapons = set()
        self.weapons.add(self.rightHandWeapon)
        self.vest = 0

    def setFullVest(self):
        self.vest = 100
