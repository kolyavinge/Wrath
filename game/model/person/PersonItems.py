from game.model.weapon.Rifle import Rifle


class PersonItems:

    def __init__(self):
        self.rightHandWeapon = Rifle()
        self.leftHandWeapon = None
        self.currentWeapon = self.rightHandWeapon
        self.weapons = set()
        self.weapons.add(self.rightHandWeapon)
        self.vest = 0

    def setFullVest(self):
        self.vest = 100
