class Vector4:

    def __init__(self, x, y, z, w):
        self.x = x
        self.y = y
        self.z = z
        self.w = w

    # convert to Normalized Device Coordinates
    def toNDC(self):
        self.x /= self.w
        self.y /= self.w
        self.z /= self.w
        self.w = 1.0
