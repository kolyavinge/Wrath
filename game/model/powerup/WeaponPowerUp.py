from game.calc.Geometry import Geometry
from game.lib.Random import Random
from game.model.powerup.Powerup import Powerup
from game.model.weapon.Rifle import Rifle
from game.model.weapon.Weapon import Weapon


class WeaponPowerup(Powerup):

    def __init__(self):
        super().__init__()
        self.height = 1.5
        rand = Random()
        weaponTypes = Weapon.getAllWeaponTypes()
        self.weaponType = weaponTypes[rand.getInt(0, len(weaponTypes))]
        self.weaponType = Rifle  # TODO

    def update(self):
        self.rotateRadians = Geometry.normalizeRadians(self.rotateRadians + 0.1)
