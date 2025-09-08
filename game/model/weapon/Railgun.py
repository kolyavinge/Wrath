from game.calc.Vector3 import Vector3
from game.model.Material import Material
from game.model.weapon.Bullet import Bullet
from game.model.weapon.BulletHoleInfo import BulletHoleInfo
from game.model.weapon.BulletTrace import BulletTrace
from game.model.weapon.Weapon import Weapon


class RailgunBulletTrace(BulletTrace):

    def __init__(self):
        super().__init__()
        self.fade = 0.01
        self.material = Material.railgunBulletTrace


class RailgunBullet(Bullet):
    def __init__(self):
        super().__init__(RailgunBulletTrace)
        self.velocityValue = 3
        self.damagePercent = 0.8
        self.goThroughPerson = True
        self.damagedPersonSet = set()
        self.paralyze = True
        self.paralyzeTime = 100
        self.holeInfo = BulletHoleInfo.railgunHole


class Railgun(Weapon):

    def __init__(self):
        super().__init__(RailgunBullet)
        self.barrelPoint = Vector3(0.003, -0.02, 0.01)
        self.bulletsCount = 10
        self.maxBulletsCount = 10
        self.delay = 50
        self.jitterFade = 0.9
        self.jitterDelta = 0.05
        self.feedbackFade = 0.6
        self.feedbackLength = 0.05
        self.playerShift = Vector3(0.1, 0.3, -0.11)
        self.enemyShift = Vector3(0.16, 0.5, -0.1)
        self.selectionShift = Vector3(0, -0.25, 0)
