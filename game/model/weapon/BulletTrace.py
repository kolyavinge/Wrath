from game.calc.Vector3 import Vector3


class BulletTrace:

    def __init__(self):
        self.bullet = None
        self.startPosition = Vector3()
        self.currentPosition = Vector3()
        self.brightness = 1.0
        self.fade = 0.9
        self.isVisible = True
        self.material = None
        self.visibilityLevelSegments = set()

    def update(self):
        self.brightness *= self.fade
        if self.brightness < 0.01:
            self.isVisible = False
            self.brightness = 0.0
