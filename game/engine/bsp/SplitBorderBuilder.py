from game.engine.bsp.SplitBorder import SplitBorder


class SplitBorderBuilder:

    def getFrontSplitBorder(self, splitBorder, basePoint, frontNormal):
        if frontNormal.z == 1:
            return SplitBorder(splitBorder.minX, splitBorder.maxX, splitBorder.minY, splitBorder.maxY, basePoint.z, splitBorder.maxZ)
        elif frontNormal.z == -1:
            return SplitBorder(splitBorder.minX, splitBorder.maxX, splitBorder.minY, splitBorder.maxY, splitBorder.minZ, basePoint.z)
        elif frontNormal.y == 1:
            return SplitBorder(splitBorder.minX, splitBorder.maxX, basePoint.y, splitBorder.maxY, splitBorder.minZ, splitBorder.maxZ)
        elif frontNormal.y == -1:
            return SplitBorder(splitBorder.minX, splitBorder.maxX, splitBorder.minY, basePoint.y, splitBorder.minZ, splitBorder.maxZ)
        elif frontNormal.x == 1:
            return SplitBorder(basePoint.x, splitBorder.maxX, splitBorder.minY, splitBorder.maxY, splitBorder.minZ, splitBorder.maxZ)
        elif frontNormal.x == -1:
            return SplitBorder(splitBorder.minX, basePoint.x, splitBorder.minY, splitBorder.maxY, splitBorder.minZ, splitBorder.maxZ)
        else:
            raise Exception()

    def getBackSplitBorder(self, splitBorder, basePoint, frontNormal):
        if frontNormal.z == 1:
            return SplitBorder(splitBorder.minX, splitBorder.maxX, splitBorder.minY, splitBorder.maxY, splitBorder.minZ, basePoint.z)
        elif frontNormal.z == -1:
            return SplitBorder(splitBorder.minX, splitBorder.maxX, splitBorder.minY, splitBorder.maxY, basePoint.z, splitBorder.maxZ)
        elif frontNormal.y == 1:
            return SplitBorder(splitBorder.minX, splitBorder.maxX, splitBorder.minY, basePoint.y, splitBorder.minZ, splitBorder.maxZ)
        elif frontNormal.y == -1:
            return SplitBorder(splitBorder.minX, splitBorder.maxX, basePoint.y, splitBorder.maxY, splitBorder.minZ, splitBorder.maxZ)
        elif frontNormal.x == 1:
            return SplitBorder(splitBorder.minX, basePoint.x, splitBorder.minY, splitBorder.maxY, splitBorder.minZ, splitBorder.maxZ)
        elif frontNormal.x == -1:
            return SplitBorder(basePoint.x, splitBorder.maxX, splitBorder.minY, splitBorder.maxY, splitBorder.minZ, splitBorder.maxZ)
        else:
            raise Exception()


def makeSplitBorderBuilder(resolver):
    return SplitBorderBuilder()
