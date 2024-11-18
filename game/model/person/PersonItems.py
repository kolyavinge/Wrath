from game.model.weapon.Pistol import Pistol
from game.model.weapon.Rifle import Rifle


class PersonItems:

    def __init__(self):
        self.rightHandWeapon = Pistol()
        self.leftHandWeapon = Pistol()
        self.currentWeapon = self.rightHandWeapon
        self.weapons = set()
        self.weapons.add(self.rightHandWeapon)
        self.weapons.add(self.leftHandWeapon)
        self.vest = 0

    def setFullVest(self):
        self.vest = 100
