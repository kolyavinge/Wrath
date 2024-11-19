from game.calc.Vector3 import Vector3
from game.model.weapon.BulletHoleInfo import BulletHoleInfo
from game.model.weapon.Weapon import Bullet, Weapon


class PlasmaBullet(Bullet):

    def __init__(self):
        super().__init__()
        self.velocityValue = 5
        self.damage = 5
        self.holeInfo = BulletHoleInfo.tinyHole


class Plasma(Weapon):

    def __init__(self):
        super().__init__(PlasmaBullet, None)
        self.barrelPoint = Vector3(0, 0.3, 0.03)
        self.bulletsCount = 50
        self.maxBulletsCount = 50
        self.delay = 8
        self.jitterFade = 0.9
        self.jitterDelta = 0.05
        self.feedbackFade = 0.6
        self.feedbackLength = 0.05
        self.playerShift = Vector3(0.06, 0.15, -0.05)
