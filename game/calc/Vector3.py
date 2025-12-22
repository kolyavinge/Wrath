from game.lib.Math import Math
from game.lib.Numeric import Numeric
from game.lib.Random import Random


class Vector3:

    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.set(x, y, z)

    def set(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def copy(self):
        return Vector3(self.x, self.y, self.z)

    def copyFrom(self, vector):
        self.x = vector.x
        self.y = vector.y
        self.z = vector.z

    def getLength(self):
        return Math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)

    def setLength(self, newLength):
        if newLength < 0:
            raise Exception("Length cannot be negative.")

        length = self.getLength()
        self.mul(newLength / length)

    def isZero(self):
        return Numeric.floatEquals(self.x, 0.0) and Numeric.floatEquals(self.y, 0.0) and Numeric.floatEquals(self.z, 0.0)

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

    def getNormalized(self):
        v = self.copy()
        v.normalize()

        return v

    def dotProduct(self, vector):
        return self.x * vector.x + self.y * vector.y + self.z * vector.z

    def vectorProduct(self, vector):
        x = self.y * vector.z - self.z * vector.y
        y = self.z * vector.x - self.x * vector.z
        z = self.x * vector.y - self.y * vector.x
        self.x = x
        self.y = y
        self.z = z

    def isParallel(self, vector, eps=0.001):
        value = self.dotProduct(vector) / (self.getLength() * vector.getLength())
        return Numeric.floatEquals(value, 1, eps)

    def getDirectionTo(self, vector):
        direction = vector.copy()
        direction.sub(self)

        return direction

    def getLengthTo(self, vector):
        dx = self.x - vector.x
        dy = self.y - vector.y
        dz = self.z - vector.z

        return Math.sqrt(dx * dx + dy * dy + dz * dz)

    def getMiddleTo(self, vector):
        middle = self.getDirectionTo(vector)
        middle.div(2)
        middle.add(self)

        return middle

    def round(self):
        if Numeric.floatEquals(self.x, 0):
            self.x = 0
        if Numeric.floatEquals(self.y, 0):
            self.y = 0
        if Numeric.floatEquals(self.z, 0):
            self.z = 0

    def reflectBy(self, normal):
        # reflected = vector - 2 * (vector * normal) * normal
        product = 2.0 * (self.x * normal.x + self.y * normal.y + self.z * normal.z)
        self.x -= product * normal.x
        self.y -= product * normal.y
        self.z -= product * normal.z

    def __eq__(self, vector):
        return self.x == vector.x and self.y == vector.y and self.z == vector.z

    def __hash__(self):
        return hash((self.x, self.y, self.z))

    def __str__(self):
        return f"{self.x:.2f} : {self.y:.2f} : {self.z:.2f}"

    @staticmethod
    def calcDirectionAndGetDotProduct(startPoint, endPoint, vectorForDotProduct):
        x = endPoint.x - startPoint.x
        y = endPoint.y - startPoint.y
        z = endPoint.z - startPoint.z
        dotProduct = x * vectorForDotProduct.x + y * vectorForDotProduct.y + z * vectorForDotProduct.z

        return dotProduct

    @staticmethod
    def fromStartToEnd(startPoint, endPoint, stepLength):
        stepDirection = startPoint.getDirectionTo(endPoint)
        stepsCount = int(stepDirection.getLength() / stepLength)
        stepDirection.setLength(stepLength)
        yield startPoint.copy()
        point = startPoint.copy()
        for _ in range(stepsCount - 1):
            point.add(stepDirection)
            yield point.copy()
        yield endPoint.copy()

    @staticmethod
    def getRandomNormalVector():
        x = Random.getFloat(-1.0, 1.0)
        y = Random.getFloat(-1.0, 1.0)
        z = Random.getFloat(-1.0, 1.0)
        result = Vector3(x, y, z)
        result.normalize()

        return result

    @staticmethod
    def getLinearInterpolatedVector(a, b, t):
        # a * (1.0 - t) + b * t

        k = 1.0 - t
        x = a.x * k + b.x * t
        y = a.y * k + b.y * t
        z = a.z * k + b.z * t

        return Vector3(x, y, z)
