from game.calc.Geometry import Geometry
from game.lib.Math import Math


class DefaultAimState:

    def __init__(self):
        self.verticalViewRadians = Geometry.degreesToRadians(45.0)
        self.mouseSensibility = 0.004


class SniperAimState:

    def __init__(self):
        self.verticalViewRadiansMax = Geometry.degreesToRadians(15.0)
        self.verticalViewRadiansMin = Geometry.degreesToRadians(2.0)
        self.radiansStep = Geometry.degreesToRadians(2.0)
        self.verticalViewRadians = self.verticalViewRadiansMax
        self.mouseSensibility = 0.0005

    def zoomIn(self):
        self.verticalViewRadians = Math.max(self.verticalViewRadians - self.radiansStep, self.verticalViewRadiansMin)

    def zoomOut(self):
        self.verticalViewRadians = Math.min(self.verticalViewRadians + self.radiansStep, self.verticalViewRadiansMax)
