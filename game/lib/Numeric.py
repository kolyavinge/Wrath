from game.lib.Math import Math


class Numeric:

    @staticmethod
    def floatEquals(x, y, eps=0.000000001):
        return Math.abs(x - y) < eps

    @staticmethod
    def between(x, left, right):
        return left <= x and x <= right

    @staticmethod
    def isPowerOf2(x):
        if x <= 0:
            return False

        while True:
            if x == 1.0:
                return True
            elif x % 2 == 0:
                x /= 2
            else:
                return False

    @staticmethod
    def isOdd(x):
        return (x % 2) != 0

    @staticmethod
    def limitBy(value, leftLimit, rightLimit):
        if value < leftLimit:
            return leftLimit
        elif value > rightLimit:
            return rightLimit
        else:
            return value

    @staticmethod
    def limitMin(value, threshold, minValue):
        if value < threshold:
            return minValue
        else:
            return value

    @staticmethod
    def limitMax(value, threshold, maxValue):
        if value > threshold:
            return maxValue
        else:
            return value
