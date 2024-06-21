from game.lib.Math import Math


class Numeric:

    @staticmethod
    def floatEquals(x, y, eps):
        return Math.abs(x - y) < eps
