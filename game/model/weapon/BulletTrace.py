from game.calc.Vector3 import Vector3
from game.lib.DecrementCounter import DecrementCounter


class BulletTrace:

    def __init__(self):
        self.bullet = None
        self.startPosition = Vector3()
        self.currentPosition = Vector3()
        self.isVisible = True
        self.visibilityLevelSegments = set()
        self.aliveRemainCounter = DecrementCounter()

    def update(self):
        if not self.bullet.isAlive:
            self.aliveRemainCounter.decrease()
            if self.aliveRemainCounter.isExpired():
                self.isVisible = False


class RayBulletTrace(BulletTrace):

    def __init__(self):
        super().__init__()
        self.brightness = 1.0
        self.fade = 0.9
        self.material = None

    def update(self):
        self.brightness -= self.fade
        if self.brightness < 0.01:
            self.isVisible = False
            self.brightness = 0.0
