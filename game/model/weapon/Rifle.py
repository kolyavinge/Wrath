from game.calc.Geometry import Geometry
from game.calc.Vector3 import Vector3
from game.lib.DecrementCounter import DecrementCounter
from game.model.Material import Material
from game.model.weapon.Bullet import Bullet
from game.model.weapon.BulletHoleInfo import BulletHoleInfo
from game.model.weapon.BulletTrace import RayBulletTrace
from game.model.weapon.Debris import Debris
from game.model.weapon.Explosion import Explosion
from game.model.weapon.Grenade import Grenade
from game.model.weapon.SimpleFlash import SimpleFlash
from game.model.weapon.Weapon import Weapon


class RifleFlash(SimpleFlash):

    def __init__(self):
        super().__init__()


class RifleBulletTrace(RayBulletTrace):

    def __init__(self):
        super().__init__()
        self.fade = 0.1
        self.material = Material.commonBulletTrace


class RifleBullet(Bullet):

    def __init__(self):
        super().__init__(RifleBulletTrace)
        self.velocityValue = 16
        self.damagePercent = 0.2
        self.ricochetPossibility = 0.2
        self.holeInfo = BulletHoleInfo.smallHole


class RifleGrenadeExplosion(Explosion):

    def __init__(self):
        super().__init__(Debris)
        self.maxRadius = 4
        self.velocityValue = 0.1
        self.damagePercent = 0.02
        self.debrisCount = 8
        self.aliveRemainCounter.set(150)


class RifleGrenade(Grenade):

    def __init__(self):
        super().__init__(None, RifleGrenadeExplosion)
        self.velocityValue = 0.5
        self.accelValue = 0.05
        self.gravityValue = 0.01
        self.damagePercent = 0
        self.ricochetVelocityCoeff = 0.2
        self.holeInfo = BulletHoleInfo.explosionHole
        self.detonationTimeout = DecrementCounter(50)

    def update(self):
        self.rollRadians = Geometry.normalizeRadians(self.pitchRadians + 0.1)


class Rifle(Weapon):

    hasAltBulletDebris = True

    def __init__(self):
        super().__init__(RifleBullet, RifleFlash, RifleGrenade)
        self.barrelPoint = Vector3(0, 0.4, 0.04)
        self.isBurstModeEnabled = True
        self.minBurstCount = 1
        self.maxBurstCount = 4
        self.bulletsCount = 50
        self.maxBulletsCount = 50
        self.altBulletsCount = 10
        self.maxAltBulletsCount = 10
        self.delay = 4
        self.altDelay = 25
        self.jitterFade = 0.9
        self.jitterDelta = 0.05
        self.feedbackFade = 0.6
        self.feedbackLength = 0.05
        self.playerShift = Vector3(0.1, 0.2, -0.11)
        self.enemyShift = Vector3(0.15, 0.3, -0.1)
        self.selectionShift = Vector3(0, -0.25, 0)
