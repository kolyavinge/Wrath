import numpy


class Matrix3:

    def __init__(self, items):
        self.items = items

    def toFloat32Array(self):
        return numpy.array(self.items, dtype=numpy.float32)
