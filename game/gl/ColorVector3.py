class ColorVector3:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def normalize(self):
        self.x /= 256
        self.y /= 256
        self.z /= 256
