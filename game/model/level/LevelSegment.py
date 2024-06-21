class LevelSegment:

    def __init__(self, minX, maxX, minY, maxY, minZ, maxZ):
        self.minX = minX
        self.maxX = maxX
        self.minY = minY
        self.maxY = maxY
        self.minZ = minZ
        self.maxZ = maxZ
        self.walls = []
