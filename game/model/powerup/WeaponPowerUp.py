from game.calc.Geometry import Geometry
from game.lib.Random import Random
from game.model.powerup.Powerup import Powerup
from game.model.weapon.Weapon import Weapon


class WeaponPowerup(Powerup):

    def __init__(self):
        super().__init__()
        self.height = 0.5
        rand = Random()
        weaponTypes = Weapon.getAllWeaponTypes()
        self.weaponType = weaponTypes[rand.getInt(0, len(weaponTypes))]

    def update(self):
        self.rotateRadians = Geometry.normalizeRadians(self.rotateRadians + 0.01)
