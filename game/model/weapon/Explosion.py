from game.calc.Vector3 import Vector3
from game.lib.DecrementCounter import DecrementCounter


class Explosion:

    def __init__(self):
        self.bullet = None
        self.radius = 0
        self.maxRadius = 0
        self.velocityValue = 0
        self.position = Vector3()
        self.damagePercent = 0
        self.isVisible = True
        self.aliveRemainCounter = DecrementCounter()
        self.collisionLevelSegment = None
        self.visibilityLevelSegment = None

    def update(self):
        if self.radius >= 0:
            self.radius += self.velocityValue
            if self.radius > self.maxRadius:
                self.radius = -1
        else:
            self.aliveRemainCounter.decrease()
            if self.aliveRemainCounter.isExpired():
                self.isVisible = False
