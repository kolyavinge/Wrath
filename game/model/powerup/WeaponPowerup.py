from game.anx.PlayerConstants import PlayerConstants
from game.calc.Geometry import Geometry
from game.lib.CircularIterator import CircularIterator
from game.lib.Random import Random
from game.model.powerup.Powerup import Powerup
from game.model.weapon.Weapon import Weapon


class WeaponPowerup(Powerup):

    def __init__(self):
        super().__init__()
        self.height = PlayerConstants.eyeLength - 0.2
        rand = Random()
        weaponTypes = Weapon.getAllWeaponTypes()
        self.weaponType = weaponTypes[rand.getInt(0, len(weaponTypes))]
        shift = 0.002
        self.zShift = CircularIterator([shift for _ in range(0, 20)] + [-shift for _ in range(0, 20)])

    def update(self):
        self.position.z += self.zShift.getItem()
        self.zShift.move()
        self.rotateRadians = Geometry.normalizeRadians(self.rotateRadians + 0.1)
