from game.calc.Geometry import Geometry
from game.calc.Vector3 import Vector3
from game.lib.Math import Math
from game.lib.Random import Random
from game.model.weapon.Bullet import Bullet
from game.model.weapon.BulletHoleInfo import BulletHoleInfo
from game.model.weapon.Weapon import Weapon


class PlasmaBullet(Bullet):

    def __init__(self):
        super().__init__()
        self.isVisible = True
        self.velocityValue = 0.5
        self.damagePercent = 0.25
        self.holeInfo = BulletHoleInfo.plasmaHole
        rand = Random()
        self.pitchRadians = rand.getFloat(0, Math.piDouble)
        self.yawRadians = rand.getFloat(0, Math.piDouble)

    def update(self):
        self.pitchRadians = Geometry.normalizeRadians(self.pitchRadians + 0.1)
        self.yawRadians = Geometry.normalizeRadians(self.yawRadians + 0.1)


class Plasma(Weapon):

    def __init__(self):
        super().__init__(PlasmaBullet)
        self.barrelPoint = Vector3(0, 0.3, 0)
        self.bulletsCount = 50
        self.maxBulletsCount = 50
        self.delay = 15
        self.jitterFade = 0.9
        self.jitterDelta = 0.05
        self.feedbackFade = 0.6
        self.feedbackLength = 0.05
        self.playerShift = Vector3(0.1, 0.3, -0.12)
        self.enemyShift = Vector3(0.15, 0.4, -0.1)
