from game.calc.Vector3 import Vector3
from game.lib.DecrementCounter import DecrementCounter
from game.model.weapon.ExplosionKind import ExplosionKind


class Explosion:

    def __init__(self, debrisType=None):
        self.id = 0
        self.kind = ExplosionKind.unknown
        self.debrisType = debrisType
        self.bullet = None
        self.radius = 0
        self.maxRadius = 0
        self.velocityValue = 0
        self.position = Vector3()
        self.damagePercent = 0
        self.debrisCount = 0
        self.isVisible = True
        self.aliveRemainCounter = DecrementCounter()
        self.collisionLevelSegment = None
        self.visibilityLevelSegment = None
        self.initTimeSec = 0

    def update(self):
        if self.radius >= 0:
            self.radius += self.velocityValue
            if self.radius > self.maxRadius:
                self.radius = -1
        else:
            self.aliveRemainCounter.decrease()
            if self.aliveRemainCounter.isExpired():
                self.isVisible = False
