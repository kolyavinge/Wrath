from game.model.Material import Material
from game.model.weapon.Bullet import Bullet
from game.model.weapon.BulletHoleInfo import BulletHoleInfo
from game.model.weapon.BulletTrace import RayBulletTrace


class DebrisBulletTrace(RayBulletTrace):

    def __init__(self):
        super().__init__()
        self.fade = 0.1
        self.material = Material.commonBulletTrace


class Debris(Bullet):

    def __init__(self):
        super().__init__(DebrisBulletTrace)
        self.velocityValue = 1
        self.damagePercent = 0.05
        self.canDamageOwner = True
        self.canIncreaseFrags = False
        self.holeInfo = BulletHoleInfo.smallHole
