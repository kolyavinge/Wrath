from game.calc.Vector3 import Vector3
from game.model.weapon.BulletHoleInfo import BulletHoleInfo
from game.model.weapon.SimpleFlash import SimpleFlash
from game.model.weapon.Weapon import Bullet, Weapon


class PistolFlash(SimpleFlash):

    def __init__(self):
        super().__init__()


class PistolBullet(Bullet):

    def __init__(self):
        super().__init__()
        self.velocityValue = 2
        self.damage = 5
        self.holeInfo = BulletHoleInfo.smallHole


class Pistol(Weapon):

    defaultCount = 2

    def __init__(self):
        super().__init__(PistolBullet, PistolFlash)
        self.barrelPoint = Vector3(0, 0.1, 0.01)
        self.bulletsCount = 25
        self.maxBulletsCount = 25
        self.delay = 10
        self.jitterFade = 0.9
        self.jitterDelta = 0.05
        self.feedbackFade = 0.6
        self.feedbackLength = 0.05
        self.playerShift = Vector3(0.12, 0.3, -0.1)
