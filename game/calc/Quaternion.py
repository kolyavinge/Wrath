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
        pivot = fromVector.copy()
        pivot.vectorProduct(toVector)
        if not pivot.isZero():
            self.setAngleAndPivot(alpha, pivot)
        else:
            self.setIdentity()

    def getAngleAndPivot(self):
        alphaHalf = Math.arccos(self.w)
        radians = 2.0 * alphaHalf
        pivot = Vector3(self.x, self.y, self.z)
        sinHalf = Math.sin(alphaHalf)
        if not Numeric.floatEquals(sinHalf, 0.0):
            pivot.div(sinHalf)
        if pivot.isZero():
            pivot.set(0.0, 0.0, 1.0)

        return (radians, pivot)

    def setAngleAndPivot(self, radians, pivot):
        sinHalf = Math.sin(radians / 2.0)
        cosHalf = Math.cos(radians / 2.0)
        pivot.normalize()
        pivot.mul(sinHalf)
        self.setComponents(cosHalf, pivot.x, pivot.y, pivot.z)

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

    def copy(self):
        q = Quaternion()
        q.w = self.w
        q.x = self.x
        q.y = self.y
        q.z = self.z

        return q
