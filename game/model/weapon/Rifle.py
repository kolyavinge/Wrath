from game.calc.Vector3 import Vector3
from game.model.weapon.BulletHoleInfo import BulletHoleInfo
from game.model.weapon.Weapon import Bullet, Flash, Weapon


class RifleFlash(Flash):

    def __init__(self):
        super().__init__()
        self.alphaSteps = [0.5, 0.75, 1.0, 0.75, 0.5, 0.25]
        self.alphaStep = 0
        self.alpha = 0.25

    def update(self):
        self.alphaStep += 1
        if self.alphaStep < len(self.alphaSteps):
            self.alpha = self.alphaSteps[self.alphaStep]
        else:
            self.isVisible = False
            self.alpha = 0


class RifleBullet(Bullet):

    def __init__(self):
        super().__init__()
        self.velocityValue = 5
        self.damage = 5
        self.holeInfo = BulletHoleInfo.tinyHole


class Rifle(Weapon):

    def __init__(self):
        super().__init__(RifleBullet, RifleFlash)
        self.barrelPoint = Vector3(0, 0.25, 0.03)
        self.bulletsCount = 200
        self.maxBulletsCount = 200
        self.delay = 8
        self.jitterFade = 0.9
        self.jitterDelta = 0.05
        self.feedbackFade = 0.6
        self.feedbackLength = 0.05
        self.playerShift = Vector3(0.08, 0.2, -0.1)
