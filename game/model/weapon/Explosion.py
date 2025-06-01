from game.calc.Vector3 import Vector3


class Explosion:

    def __init__(self):
        self.radius = 0
        self.maxRadius = 0
        self.velocityValue = 0
        self.position = Vector3()
        self.damagePercent = 0
        self.isVisible = True
        self.collisionLevelSegment = None
        self.visibilityLevelSegment = None

    def update(self):
        self.radius += self.velocityValue
        if self.radius > self.maxRadius:
            self.isVisible = False
            self.radius = 0
