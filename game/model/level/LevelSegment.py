class LevelSegment:

    @staticmethod
    def makeFromSplitBorder(splitBorder):
        result = LevelSegment()
        result.minX = splitBorder.minX
        result.maxX = splitBorder.maxX
        result.minY = splitBorder.minY
        result.maxY = splitBorder.maxY
        result.minZ = splitBorder.minZ
        result.maxZ = splitBorder.maxZ

        return result

    def __init__(self):
        self.minX = 0
        self.maxX = 0
        self.minY = 0
        self.maxY = 0
        self.minZ = 0
        self.maxZ = 0
        self.walls = []
        self.ground = None
