from game.anx.CommonConstants import CommonConstants
from game.calc.Geometry import Geometry
from game.calc.Plane import Plane
from game.calc.Vector3 import Vector3
from game.lib.DecrementCounter import DecrementCounter
from game.lib.Math import Math
from game.lib.Random import Random
from game.model.weapon.ExplosionKind import ExplosionKind


class Explosion:

    def __init__(self, debrisType=None):
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

    def makeDebris(self):
        if self.debrisType is None:
            return None

        result = []
        for _ in range(0, self.debrisCount):
            debris = self.debrisType()
            debris.currentPosition = self.position.copy()
            debris.nextPosition = debris.currentPosition.copy()
            debris.directionTopNormal = Vector3(Random.getFloat(-0.1, 0.1), Random.getFloat(-0.1, 0.1), 1.0)
            debris.directionTopNormal.normalize()
            plane = Plane(debris.directionTopNormal, CommonConstants.axisOrigin)
            debris.direction = Geometry.rotatePoint(
                plane.getAnyVector(), debris.directionTopNormal, CommonConstants.axisOrigin, Random.getFloat(-Math.piDouble, Math.piDouble)
            )
            debris.direction.normalize()
            debris.velocity = debris.direction.copy()
            debris.velocity.setLength(debris.velocityValue)
            result.append(debris)

        return result

    def update(self):
        if self.radius >= 0:
            self.radius += self.velocityValue
            if self.radius > self.maxRadius:
                self.radius = -1
        else:
            self.aliveRemainCounter.decrease()
            if self.aliveRemainCounter.isExpired():
                self.isVisible = False
