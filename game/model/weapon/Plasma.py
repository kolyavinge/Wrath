from game.calc.Geometry import Geometry
from game.calc.Vector3 import Vector3
from game.lib.Math import Math
from game.lib.Random import Random
from game.model.weapon.Bullet import Bullet
from game.model.weapon.BulletHoleInfo import BulletHoleInfo
from game.model.weapon.Explosion import Explosion
from game.model.weapon.Ray import Ray
from game.model.weapon.Weapon import Weapon


class PlasmaExplosion(Explosion):

    def __init__(self):
        super().__init__()
        self.velocityValue = 0.1
        self.particlesInGroup = 1000
        self.particleGroupsCount = 10
        self.particleAppearanceDelayMsec = 10
        self.particleLifeTimeMsec = 500
        self.particleSize = 0.01
        self.aliveRemainCounter.set(50)


class PlasmaBullet(Bullet):

    def __init__(self):
        super().__init__(None, PlasmaExplosion)
        self.isVisible = True
        self.velocityValue = 0.8
        self.damagePercent = 0.25
        self.holeInfo = BulletHoleInfo.plasmaHole
        self.pitchRadians = Random.getFloat(0, Math.piDouble)
        self.yawRadians = Random.getFloat(0, Math.piDouble)
        self.targetPerson = None
        self.homingDistance = 20.0
        self.homingFieldViewRadians = Geometry.degreesToRadians(10.0)
        self.homingFieldViewRadiansCos = Math.cos(self.homingFieldViewRadians)
        self.homingRadians = Geometry.degreesToRadians(0.5)

    def update(self):
        self.pitchRadians = Geometry.normalizeRadians(self.pitchRadians + 0.1)
        self.yawRadians = Geometry.normalizeRadians(self.yawRadians + 0.1)


class PlasmaRay(Ray):

    def __init__(self):
        super().__init__()
        self.maxLength = 10
        self.velocityValue = 0.5
        self.damagePercent = 0.01


class Plasma(Weapon):

    def __init__(self):
        super().__init__(PlasmaBullet)
        self.barrelPoint = Vector3(0.0, 0.35, 0.025)
        self.isBurstModeEnabled = True
        self.minBurstCount = 1
        self.maxBurstCount = 5
        self.bulletsCount = 50
        self.maxBulletsCount = 50
        self.delay = 15
        self.jitterFade = 0.9
        self.jitterDelta = 0.05
        self.feedbackFade = 0.6
        self.feedbackLength = 0.05
        self.playerShift = Vector3(0.1, 0.3, -0.12)
        self.enemyShift = Vector3(0.15, 0.4, -0.1)
        self.selectionShift = Vector3(0, -0.3, 0)

    def makeRay(self, ownerPerson):
        ray = PlasmaRay()
        ray.startPosition = self.barrelPosition
        ray.currentPosition = ray.startPosition
        ray.weapon = self
        ray.ownerPerson = ownerPerson

        return ray
