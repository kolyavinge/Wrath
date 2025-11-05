from game.calc.Geometry import Geometry
from game.lib.Math import Math
from game.lib.Random import Random


class DefaultAimState:

    def __init__(self):
        self.verticalViewRadians = Geometry.degreesToRadians(45.0)
        self.mouseSensibility = 0.004


class SniperAimFloatingFunc:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def getValue(self, x):
        return self.a * Math.sin(self.b * x)


class SniperAimState:

    def __init__(self):
        self.verticalViewRadiansMax = Geometry.degreesToRadians(15.0)
        self.verticalViewRadiansMin = Geometry.degreesToRadians(2.0)
        self.radianStep = Geometry.degreesToRadians(2.0)
        self.verticalViewRadians = self.verticalViewRadiansMax
        self.mouseSensibility = 0.0003
        self.aFloatingFunc = SniperAimFloatingFunc(Random.getOneOrMinusOne() * 0.0025, Random.getOneOrMinusOne() * 0.04)
        self.bFloatingFunc = SniperAimFloatingFunc(Random.getOneOrMinusOne() * 0.002, Random.getOneOrMinusOne() * 0.05)
        self.aFloatingParam = 0
        self.bFloatingParam = 0
        self.aFloatingValue = self.aFloatingFunc.getValue(self.aFloatingParam)
        self.bFloatingValue = self.bFloatingFunc.getValue(self.bFloatingParam)

    def zoomIn(self):
        self.verticalViewRadians = Math.max(self.verticalViewRadians - self.radianStep, self.verticalViewRadiansMin)

    def zoomOut(self):
        self.verticalViewRadians = Math.min(self.verticalViewRadians + self.radianStep, self.verticalViewRadiansMax)
