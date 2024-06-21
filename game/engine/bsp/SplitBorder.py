class SplitBorder:

    def __init__(self, minX, maxX, minY, maxY, minZ, maxZ):
        self.minX = minX
        self.maxX = maxX
        self.minY = minY
        self.maxY = maxY
        self.minZ = minZ
        self.maxZ = maxZ

    def getCopy(self):
        return SplitBorder(self.minX, self.maxX, self.minY, self.maxY, self.minZ, self.maxZ)
