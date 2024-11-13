from game.anx.CommonConstants import CommonConstants
from game.calc.Geometry import Geometry
from game.calc.Vector3 import Vector3
from game.lib.Math import Math


class Ellipse:

    def __init__(self, a, b, centerX, centerY, step):
        # уравнение эллипса
        # (x² / a²) + (y² / b²) = 1

        self.a = a
        self.a2 = a * a
        self.b = b
        self.center = Vector3(centerX, centerY, 0)
        self.step = step
        self.calculatePoints()
        self.toCenter()

    def calculatePoints(self):
        self.points = []

        self.points.append(Vector3(self.a, 0, 0))

        x = self.a - self.step
        while x > -self.a:
            y = self.getY(x)
            self.points.append(Vector3(x, y, 0))
            x -= self.step

        self.points.append(Vector3(-self.a, 0, 0))

        x = -(self.a - self.step)
        while x < self.a:
            y = -self.getY(x)
            self.points.append(Vector3(x, y, 0))
            x += self.step

        # последняя и первая точка дублируются
        # так проще соединять их в полигоны
        self.points.append(Vector3(self.a, 0, 0))

    def getY(self, x):
        return Math.sqrt((1.0 - (x * x) / self.a2)) * self.b

    def toCenter(self):
        for p in self.points:
            p.add(self.center)

    def rotateTo(self, radians):
        self.center = Geometry.rotatePoint(self.center, CommonConstants.zAxis, CommonConstants.axisOrigin, radians)

        for p in self.points:
            rotated = Geometry.rotatePoint(p, CommonConstants.zAxis, CommonConstants.axisOrigin, radians)
            p.set(rotated.x, rotated.y, rotated.z)

    def swapYZ(self):
        t = self.center.y
        self.center.y = self.center.z
        self.center.z = t

        for p in self.points:
            t = p.y
            p.y = p.z
            p.z = t
