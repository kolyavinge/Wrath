from game.calc.Vector3 import Vector3
from game.model.Material import Material
from game.model.weapon.Bullet import Bullet
from game.model.weapon.BulletHoleInfo import BulletHoleInfo
from game.model.weapon.BulletTrace import BulletTrace
from game.model.weapon.Weapon import Weapon


class RailgunBulletTrace(BulletTrace):

    def __init__(self):
        super().__init__()
        self.material = Material.railgunBulletTrace


class RailgunBullet(Bullet):
    def __init__(self):
        super().__init__(RailgunBulletTrace)
        self.velocityValue = 1
        self.damage = 5
        self.holeInfo = BulletHoleInfo.smallHole


class Railgun(Weapon):

    def __init__(self):
        super().__init__(RailgunBullet)
        self.barrelPoint = Vector3(0, 0.3, 0.03)
        self.bulletsCount = 10
        self.maxBulletsCount = 10
        self.delay = 20
        self.jitterFade = 0.9
        self.jitterDelta = 0.05
        self.feedbackFade = 0.6
        self.feedbackLength = 0.05
        self.playerShift = Vector3(0.09, 0.25, -0.1)
