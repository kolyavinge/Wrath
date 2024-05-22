from game.lib.Math import *


class Vector3:

    def __init__(self, x=0, y=0, z=0):
        self.set(x, y, z)

    def set(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def setCopy(self, vector):
        self.x = vector.x
        self.y = vector.y
        self.z = vector.z

    def getCopy(self):
        return Vector3(self.x, self.y, self.z)

    def getLength(self):
        return Math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)

    def setLength(self, newLength):
        length = self.getLength()
        self.mul(newLength / length)

    def isZero(self):
        return self.x == 0 and self.y == 0 and self.z == 0

    def add(self, vector):
        self.x += vector.x
        self.y += vector.y
        self.z += vector.z

    def sub(self, vector):
        self.x -= vector.x
        self.y -= vector.y
        self.z -= vector.z

    def mul(self, a):
        self.x *= a
        self.y *= a
        self.z *= a

    def div(self, a):
        self.x /= a
        self.y /= a
        self.z /= a

    def normalize(self):
        length = self.getLength()
        self.div(length)

    def dotProduct(self, vector):
        return self.x * vector.x + self.y * vector.y + self.z * vector.z

    def vectorProduct(self, vector):
        x = self.y * vector.z - self.z * vector.y
        y = self.z * vector.x - self.x * vector.z
        z = self.x * vector.y - self.y * vector.x
        self.x = x
        self.y = y
        self.z = z
