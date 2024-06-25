from game.calc.Vector3 import Vector3


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
        self.floor = None

    def getCenterPoint(self):
        return Vector3(self.minX + (self.maxX - self.minX) / 2, self.minY + (self.maxY - self.minY) / 2, self.minZ + (self.maxZ - self.minZ) / 2)

    def __str__(self):
        return f"({self.minX},{self.minY}),({self.maxX},{self.maxY}),({self.minZ},{self.maxZ})"
