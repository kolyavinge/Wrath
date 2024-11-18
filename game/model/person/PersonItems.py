from game.model.weapon.Launcher import Launcher
from game.model.weapon.Pistol import Pistol
from game.model.weapon.Rifle import Rifle


class PersonItems:

    def __init__(self):
        self.rightHandWeapon = Launcher()
        self.leftHandWeapon = None
        self.currentWeapon = self.rightHandWeapon
        self.weapons = set()
        self.weapons.add(self.rightHandWeapon)
        self.vest = 0

    def setFullVest(self):
        self.vest = 100
