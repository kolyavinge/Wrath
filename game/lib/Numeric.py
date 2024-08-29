from game.lib.Math import Math


class Numeric:

    @staticmethod
    def floatEquals(x, y, eps=0.0001):
        return Math.abs(x - y) < eps

    @staticmethod
    def between(x, left, right):
        return left <= x and x <= right
