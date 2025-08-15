from game.calc.Vector3 import Vector3
from game.lib.Math import Math
from game.lib.Numeric import Numeric


class Geometry:

    degToRad = Math.pi / 180.0
    radToDeg = 180.0 / Math.pi

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

        ax = point.x * cos
        ay = point.y * cos
        az = point.z * cos

        dotProduct = pivotAxis.x * point.x + pivotAxis.y * point.y + pivotAxis.z * point.z
        m = dotProduct * (1.0 - cos)
        bx = pivotAxis.x * m
        by = pivotAxis.y * m
        bz = pivotAxis.z * m

        cx = pivotAxis.y * point.z - pivotAxis.z * point.y
        cy = pivotAxis.z * point.x - pivotAxis.x * point.z
        cz = pivotAxis.x * point.y - pivotAxis.y * point.x
        cx *= sin
        cy *= sin
        cz *= sin

        a = Vector3(ax + bx + cx, ay + by + cy, az + bz + cz)

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
        x = pointX - toX
        y = pointY - toY
        pointLengthSqr = x * x + y * y
        if pointLengthSqr < 0.01:
            return True

        x = pointX - fromX
        y = pointY - fromY
        lineX = toX - fromX
        lineY = toY - fromY
        pointLengthSqr = x * x + y * y
        if pointLengthSqr < 0.01:
            return True

        lineLengthSqr = lineX * lineX + lineY * lineY
        if pointLengthSqr > lineLengthSqr:
            return False

        vectorsLength = Math.sqrt(pointLengthSqr) * Math.sqrt(lineLengthSqr)
        if vectorsLength == 0:
            return False

        dot = (x * lineX + y * lineY) / vectorsLength

        return 0.999 <= dot and dot <= 1.001

    @staticmethod
    def getProjectedVector(vector, projectionAxis):
        newLength = vector.dotProduct(projectionAxis) / projectionAxis.getLength()
        if newLength < 0:
            raise ("Angle between vectors must be from 0 to pi/2.")

        projected = projectionAxis.copy()
        projected.setLength(newLength)

        return projected

    @staticmethod
    def getScreenProjectedPoint(modelMatrix, viewMatrix, projectionMatrix, viewport, point):
        mvpMatrix = projectionMatrix.copy()
        mvpMatrix.mul(viewMatrix)
        mvpMatrix.mul(modelMatrix)
        viewPoint = viewMatrix.mulVector3(point)
        projPoint = mvpMatrix.mulVector3(point)
        projPoint.x /= -viewPoint.z
        projPoint.y /= -viewPoint.z
        screenPoint = Vector3(
            viewport[0] + viewport[2] * (projPoint.x + 1) / 2, viewport[1] + viewport[3] * (projPoint.y + 1) / 2, (projPoint.z + 1) / 2
        )

        return screenPoint

    @staticmethod
    def getSphereIntersectPointOrNone(sphereRadius, startPoint, endPoint, delta=0.1):
        if sphereRadius < 0:
            raise Exception("sphereRadius cannot be negative.")

        hasIntersection = Numeric.between(sphereRadius, startPoint.getLength(), endPoint.getLength())
        if not hasIntersection:
            return None

        middlePoint = startPoint.getMiddleTo(endPoint)
        middlePointLength = middlePoint.getLength()

        while not Numeric.floatEquals(sphereRadius, middlePointLength, delta):
            if middlePointLength < sphereRadius:
                startPoint = middlePoint
            else:
                endPoint = middlePoint

            middlePoint = startPoint.getMiddleTo(endPoint)
            middlePointLength = middlePoint.getLength()

        return middlePoint

    def getNormalVector(base, toRight, toUp):
        normal = base.getDirectionTo(toRight)
        normal.vectorProduct(base.getDirectionTo(toUp))
        normal.normalize()

        return normal
