from game.anx.CommonConstants import CommonConstants
from game.calc.TransformMatrix4 import TransformMatrix4
from game.calc.Vector3 import Vector3
from game.lib.Random import Random
from game.model.weapon.BulletHoleInfo import BulletHoleInfo
from game.model.weapon.Weapon import Bullet, Flash, Weapon


class RifleFlash(Flash):

    def __init__(self):
        super().__init__()
        self.alphaSteps = [0.75, 1.0, 0.75, 0.5, 0.25]
        self.alphaStep = 0
        self.alpha = 0.5
        self.rand = Random()

    def update(self):
        self.alphaStep += 1
        if self.alphaStep < len(self.alphaSteps):
            self.alpha = self.alphaSteps[self.alphaStep]
        else:
            self.isVisible = False
            self.alpha = 0

    def calculateModelMatrix(self, position, yawRadians, pitchRadians):
        m1 = TransformMatrix4()
        m1.translate(position.x, position.y, position.z)

        m2 = TransformMatrix4()
        m2.rotate(yawRadians, CommonConstants.zAxis)
        m1.translate(position.x, position.y, position.z)

        rollRadians = self.rand.getFloat(-0.5, 0.5)
        m3 = TransformMatrix4()
        m3.rotate(rollRadians, CommonConstants.yAxis)

        m4 = TransformMatrix4()
        m4.rotate(pitchRadians, CommonConstants.xAxis)

        self.modelMatrix = TransformMatrix4()
        self.modelMatrix.mul(m1)
        self.modelMatrix.mul(m2)
        self.modelMatrix.mul(m3)
        self.modelMatrix.mul(m4)

    def getModelMatrix(self):
        return self.modelMatrix


class RifleBullet(Bullet):

    def __init__(self):
        super().__init__()
        self.velocityValue = 5
        self.damage = 5
        self.holeInfo = BulletHoleInfo.tinyHole


class Rifle(Weapon):

    def __init__(self):
        super().__init__(RifleBullet, RifleFlash)
        self.barrelPoint = Vector3(0, 0.3, 0.03)
        self.bulletsCount = 200
        self.maxBulletsCount = 200
        self.delay = 8
        self.jitterFade = 0.9
        self.jitterDelta = 0.05
        self.feedbackFade = 0.6
        self.feedbackLength = 0.05
        self.playerShift = Vector3(0.08, 0.2, -0.1)
