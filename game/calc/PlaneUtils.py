from game.calc.Vector3 import Vector3
from game.lib.Random import Random


class PlaneUtils:

    @staticmethod
    def getRandomPointOnPlane(plane):
        a = Random.getFloat(-100, 100)
        b = Random.getFloat(-100, 100)

        x = plane.getX(a, b)
        if x is not None:
            return Vector3(x, a, b)

        y = plane.getY(a, b)
        if y is not None:
            return Vector3(a, y, b)

        z = plane.getZ(a, b)
        return Vector3(a, b, z)
