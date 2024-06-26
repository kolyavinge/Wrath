from game.calc.Vector3 import Vector3
from game.lib.Math import Math


class Geometry:

    degToRad = Math.pi / 180
    radToDeg = 180 / Math.pi

    @staticmethod
    def normalizeRadians(radians):
        while radians > Math.piDouble:
            radians -= Math.piDouble

        while radians < -Math.piDouble:
            radians += Math.piDouble

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

        a = point.getCopy()
        a.mul(cos)

        b = pivotAxis.getCopy()
        b.mul(pivotAxis.dotProduct(point))
        b.mul(1 - cos)

        c = pivotAxis.getCopy()
        c.vectorProduct(point)
        c.mul(sin)

        a.add(b)
        a.add(c)

        # Формула Родрига

        a.add(pivotPoint)
        point.add(pivotPoint)

        return a

    @staticmethod
    def getLinesIntersectPointOrNone(from1X, from1Y, to1X, to1Y, from2X, from2Y, to2X, to2Y):
        a1 = from1Y - to1Y
        b1 = to1X - from1X
        c1 = from1X * to1Y - to1X * from1Y

        a2 = from2Y - to2Y
        b2 = to2X - from2X
        c2 = from2X * to2Y - to2X * from2Y

        denominator = a1 * b2 - a2 * b1
        if denominator == 0:
            return None

        x = (b1 * c2 - b2 * c1) / denominator
        y = (a2 * c1 - a1 * c2) / denominator

        return (x, y)

    @staticmethod
    def lineContainsPoint(fromX, fromY, toX, toY, pointX, pointY):
        intersect = Vector3(pointX - fromX, pointY - fromY, 0)
        if intersect.getLength() < 0.01:
            return True

        line = Vector3(toX - fromX, toY - fromY, 0)

        return line.isParallel(intersect) and intersect.getLength() <= line.getLength()

    @staticmethod
    def getProjectedVector(vector, projectionAxis):
        vectorLength = vector.getLength()
        dotProduct = vector.dotProduct(projectionAxis) / (vectorLength * projectionAxis.getLength())
        newLength = dotProduct * vectorLength
        projected = projectionAxis.getCopy()
        projected.setLength(newLength)

        return projected
