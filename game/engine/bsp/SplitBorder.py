class SplitBorder:

    def __init__(self, minX, maxX, minY, maxY, minZ, maxZ):
        self.minX = minX
        self.maxX = maxX
        self.minY = minY
        self.maxY = maxY
        self.minZ = minZ
        self.maxZ = maxZ

    def validate(self):
        if self.minX == self.maxX:
            raise Exception()

        if self.minY == self.maxY:
            raise Exception()

        if self.minZ == self.maxZ:
            raise Exception()

    def getCopy(self):
        return SplitBorder(self.minX, self.maxX, self.minY, self.maxY, self.minZ, self.maxZ)
