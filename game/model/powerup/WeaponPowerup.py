from game.anx.PersonConstants import PersonConstants
from game.calc.Geometry import Geometry
from game.lib.CircularIterator import CircularIterator
from game.lib.Numeric import Numeric
from game.lib.Random import Random
from game.model.powerup.Powerup import Powerup
from game.model.weapon.WeaponCollection import WeaponCollection


class WeaponPowerup(Powerup):

    def __init__(self, kind=None):
        assert kind is None or Numeric.between(kind, WeaponCollection.weaponNumbers[0], WeaponCollection.weaponNumbers[-1])
        super().__init__()
        self.height = PersonConstants.eyeLength - 0.2
        self.kind = kind or Random.getListItem(WeaponCollection.weaponNumbers)
        self.weaponType = WeaponCollection.getWeaponTypeByNumber(self.kind)
        self.count = self.weaponType.defaultCount
        self.setZShift()

    def setZShift(self):
        shift = 0.004
        self.zShift = CircularIterator([shift for _ in range(0, 20)] + [-shift for _ in range(0, 20)])

    def update(self):
        self.position.z += self.zShift.getItem()
        self.zShift.move()
        self.rotateRadians = Geometry.normalizeRadians(self.rotateRadians + 0.2)
