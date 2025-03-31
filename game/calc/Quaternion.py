from game.calc.TransformMatrix4 import TransformMatrix4
from game.calc.Vector3 import Vector3
from game.lib.Math import Math
from game.lib.Numeric import Numeric


class Quaternion:

    def __init__(self):
        self.setIdentity()

    def setComponents(self, w, x, y, z):
        self.w = w
        self.x = x
        self.y = y
        self.z = z

    def setIdentity(self):
        self.setComponents(1.0, 0.0, 0.0, 0.0)

    def setVectors(self, fromVector, toVector):
        if fromVector.isZero() or toVector.isZero():
            self.setIdentity()
            return
        dotProduct = fromVector.dotProduct(toVector)
        cosAlpha = dotProduct / (fromVector.getLength() * toVector.getLength())  # normalized vectors
        if cosAlpha > 1.0:  # float issues
            cosAlpha = 1.0
        elif cosAlpha < -1.0:
            cosAlpha = -1.0
        alpha = Math.arccos(cosAlpha)
        axis = fromVector.copy()
        axis.vectorProduct(toVector)
        if not axis.isZero():
            self.setAngleAndAxis(alpha, axis)
        else:
            self.setIdentity()

    def getAngleAndAxis(self):
        alphaHalf = Math.arccos(self.w)
        radians = 2.0 * alphaHalf
        axis = Vector3(self.x, self.y, self.z)
        sinHalf = Math.sin(alphaHalf)
        if not Numeric.floatEquals(sinHalf, 0.0):
            axis.div(sinHalf)
        if axis.isZero():
            axis.set(0.0, 0.0, 1.0)

        return (radians, axis)

    def setAngleAndAxis(self, radians, axis):
        sinHalf = Math.sin(radians / 2.0)
        cosHalf = Math.cos(radians / 2.0)
        axis.normalize()
        axis.mul(sinHalf)
        self.setComponents(cosHalf, axis.x, axis.y, axis.z)

    def inverse(self):
        self.x = -self.x
        self.y = -self.y
        self.z = -self.z

    def mul(self, q2):
        q1 = self
        w = (q1.w * q2.w) - (q1.x * q2.x) - (q1.y * q2.y) - (q1.z * q2.z)
        x = (q1.w * q2.x) + (q1.x * q2.w) + (q1.y * q2.z) - (q1.z * q2.y)
        y = (q1.w * q2.y) - (q1.x * q2.z) + (q1.y * q2.w) + (q1.z * q2.x)
        z = (q1.w * q2.z) + (q1.x * q2.y) - (q1.y * q2.x) + (q1.z * q2.w)
        self.setComponents(w, x, y, z)

    def rotatePoint(self, point):
        p = Quaternion()
        p.setComponents(0.0, point.x, point.y, point.z)

        inversed = self.copy()
        inversed.inverse()

        res = self.copy()
        res.mul(p)
        res.mul(inversed)

        return Vector3(res.x, res.y, res.z)

    def getMagnitude(self):
        return Math.sqrt(self.w * self.w + self.x * self.x + self.y * self.y + self.z * self.z)

    def normalize(self):
        mg = self.getMagnitude()
        self.w /= mg
        self.x /= mg
        self.y /= mg
        self.z /= mg

    def getTransformMatrix4(self):
        m = TransformMatrix4()
        m.items = [
            # col 1
            1.0 - 2.0 * (self.y * self.y + self.z * self.z),
            2.0 * (self.x * self.y + self.z * self.w),
            2.0 * (self.x * self.z - self.y * self.w),
            0,
            # col 2
            2.0 * (self.x * self.y - self.z * self.w),
            1.0 - 2.0 * (self.x * self.x + self.z * self.z),
            2.0 * (self.y * self.z + self.x * self.w),
            0,
            # col 3
            2.0 * (self.x * self.z + self.y * self.w),
            2.0 * (self.y * self.z - self.x * self.w),
            1.0 - 2.0 * (self.x * self.x + self.y * self.y),
            0,
            # col 4
            0,
            0,
            0,
            1,
        ]

        return m

    def isZero(self):
        return self.w == 0.0 and self.x == 0.0 and self.y == 0.0 and self.z == 0.0

    def copy(self):
        q = Quaternion()
        q.w = self.w
        q.x = self.x
        q.y = self.y
        q.z = self.z

        return q
