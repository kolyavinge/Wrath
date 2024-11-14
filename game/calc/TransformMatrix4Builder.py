from game.calc.TransformMatrix4 import TransformMatrix4


class TransformMatrix4Builder:

    def __init__(self):
        self.resultMatrix = TransformMatrix4()
        self.resultMatrix.setIdentity()

    def translate(self, x, y, z):
        m = TransformMatrix4()
        m.translate(x, y, z)
        self.resultMatrix.mul(m)

        return self

    def rotate(self, radians, axis):
        m = TransformMatrix4()
        m.rotate(radians, axis)
        self.resultMatrix.mul(m)

        return self

    def translateAndRotate(self, x, y, z, radians, axis):
        m = TransformMatrix4()
        m.translateAndRotate(x, y, z, radians, axis)
        self.resultMatrix.mul(m)

        return self

    def scale(self, x, y, z):
        m = TransformMatrix4()
        m.scale(x, y, z)
        self.resultMatrix.mul(m)

        return self
