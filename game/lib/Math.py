import math


class Math:

    pi = math.pi
    piDouble = 2 * math.pi
    piHalf = math.pi / 2

    @staticmethod
    def abs(x):
        return x if x >= 0 else -x

    @staticmethod
    def sqrt(x):
        return math.sqrt(x)

    @staticmethod
    def sin(radians):
        return math.sin(radians)

    @staticmethod
    def cos(radians):
        return math.cos(radians)

    @staticmethod
    def tan(radians):
        return math.tan(radians)

    @staticmethod
    def cotan(radians):
        return 1 / math.tan(radians)

    @staticmethod
    def ln(x):
        return math.log(x)
