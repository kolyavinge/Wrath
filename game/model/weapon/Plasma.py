from game.calc.Geometry import Geometry
from game.calc.TransformMatrix4Builder import TransformMatrix4Builder
from game.calc.Vector3 import Vector3
from game.model.weapon.BulletHoleInfo import BulletHoleInfo
from game.model.weapon.Weapon import Bullet, Weapon


class PlasmaBullet(Bullet):

    def __init__(self):
        super().__init__()
        self.isVisible = True
        self.velocityValue = 1
        self.damage = 5
        self.holeInfo = BulletHoleInfo.plasmaHole
        self.rotateRadians = 0
        self.rotateAxis = Vector3.getRandomNormalVector()

    def update(self):
        self.rotateRadians = Geometry.normalizeRadians(self.rotateRadians + 0.1)

    def getModelMatrix(self):
        return (
            TransformMatrix4Builder()
            .translate(self.currentPosition.x, self.currentPosition.y, self.currentPosition.z)
            .rotate(self.rotateRadians, self.rotateAxis)
            .resultMatrix
        )


class Plasma(Weapon):

    def __init__(self):
        super().__init__(PlasmaBullet, None)
        self.barrelPoint = Vector3(0, 0.3, 0.03)
        self.bulletsCount = 50
        self.maxBulletsCount = 50
        self.delay = 15
        self.jitterFade = 0.9
        self.jitterDelta = 0.05
        self.feedbackFade = 0.6
        self.feedbackLength = 0.05
        self.playerShift = Vector3(0.06, 0.15, -0.05)
