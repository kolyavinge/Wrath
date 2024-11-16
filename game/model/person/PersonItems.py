from game.model.weapon.Rifle import Rifle


class PersonItems:

    def __init__(self):
        self.currentWeapon = Rifle()
        self.weapons = set()
        self.weapons.add(self.currentWeapon)
        self.vest = 0

    def setFullVest(self):
        self.vest = 100
