from game.lib.Math import Math
from game.calc.Vector3 import Vector3


class Geometry:

    degToRad = Math.pi / 180
    radToDeg = 180 / Math.pi

    @staticmethod
    def normalizeRadians(radians):
        while radians > Math.piDouble:
            radians -= Math.piDouble

        return radians

    @staticmethod
    def degreesToRadians(degrees):
        return degrees * Geometry.degToRad

    @staticmethod
    def radiansToDegrees(radians):
        return radians * Geometry.radToDeg

    @staticmethod
    def rotatePoint(point, pivotAxis, pivotPoint, radians):
        point.sub(pivotPoint)

        # Формула Родрига
        # cos * point + (pivotAxis, point) * (1 - cos) * pivotAxis + sin * [pivotAxis, point]
        # a + b + c

        sin = Math.sin(radians)
        cos = Math.cos(radians)

        a = point.copy()
        a.mul(cos)

        b = pivotAxis.copy()
        b.mul(pivotAxis.dotProduct(point))
        b.mul(1 - cos)

        c = pivotAxis.copy()
        c.vectorProduct(point)
        c.mul(sin)

        a.add(b)
        a.add(c)

        # Формула Родрига

        a.add(pivotPoint)
        point.add(pivotPoint)

        return a
