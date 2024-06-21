from game.engine.bsp.SplitBorder import SplitBorder
from game.engine.bsp.SplitLineBuilder import SplitLineBuilder
from game.engine.bsp.SplitLineFrontBackPosition import SplitLineFrontBackPosition
from game.model.level.BSPTree import BSPNode
from game.model.level.LevelSegment import LevelSegment
from game.model.level.Orientation import Orientation


class BSPTreeBuilder:

    def __init__(self, splitLineBuilder):
        self.splitLineBuilder = splitLineBuilder

    def build(self, level):
        for floor in level.floors:
            maxX = max([w.getMaxX() for w in floor.walls])
            maxY = max([w.getMaxY() for w in floor.walls])
            maxZ = max([f.height for f in level.floors])
            splitBorder = SplitBorder(0, maxX, 0, maxY, 0, maxZ)
            splitLines = self.splitLineBuilder.getSplitLines(level)
            self.buildRec(floor.bspTree.root, splitLines[0].orientation, splitBorder, splitLines)

    def buildRec(self, node, splitOrientation, splitBorder, allSplitLines):
        splitLines = [s for s in allSplitLines if s.orientation == splitOrientation]
        self.sortSplitLines(splitLines)
        middleSplitLine = self.getMiddleSplitLine(splitLines)
        allSplitLines.remove(middleSplitLine)
        node.basePoint = middleSplitLine.startPoint
        node.frontNormal = middleSplitLine.frontNormal
        frontSplitLines, backSplitLines = self.getFrontAndBackSplitLines(allSplitLines, node.basePoint, node.frontNormal)
        newSplitOrientation = self.getNewSplitOrientation(splitOrientation, middleSplitLine)
        node.front = BSPNode()
        splitBorder = self.getFrontSplitBorder(splitBorder, node.basePoint, node.frontNormal)
        if frontSplitLines:
            self.buildRec(node.front, newSplitOrientation, splitBorder, frontSplitLines)
        else:
            node.front.levelSegment = LevelSegment(
                splitBorder.minX, splitBorder.maxX, splitBorder.minY, splitBorder.maxY, splitBorder.minZ, splitBorder.maxZ
            )
        if backSplitLines:
            node.back = BSPNode()
            splitBorder = self.getBackSplitBorder(splitBorder, node.basePoint, node.frontNormal)
            self.buildRec(node.back, newSplitOrientation, splitBorder, backSplitLines)

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

    def getFrontAndBackSplitLines(self, splitLines, basePoint, frontNormal):
        front = []
        back = []
        for splitLine in splitLines:
            position = self.getFrontBackPosition(splitLine, basePoint, frontNormal)
            if position == SplitLineFrontBackPosition.frontBack:
                front.append(splitLine)
                back.append(splitLine)
            elif position == SplitLineFrontBackPosition.front:
                front.append(splitLine)
            elif position == SplitLineFrontBackPosition.back:
                back.append(splitLine)
            else:  # SplitLineFrontBackPosition.parallel
                pass  # ignore this split line

        return (front, back)

    def getFrontBackPosition(self, splitLine, basePoint, frontNormal):
        direction = splitLine.startPoint.getCopy()
        direction.sub(basePoint)
        dotProductStart = direction.dotProduct(frontNormal)

        direction = splitLine.endPoint.getCopy()
        direction.sub(basePoint)
        dotProductEnd = direction.dotProduct(frontNormal)

        if dotProductStart >= 0 and dotProductEnd >= 0:
            return SplitLineFrontBackPosition.front
        elif dotProductStart < 0 and dotProductEnd < 0:
            return SplitLineFrontBackPosition.back
        elif dotProductStart * dotProductEnd < 0:
            return SplitLineFrontBackPosition.frontBack
        else:
            return SplitLineFrontBackPosition.back

    def getNewSplitOrientation(self, splitOrientation, middleSplitLine):
        if middleSplitLine.orientationCanChange:
            return Orientation.getOpposite(splitOrientation)
        else:
            return splitOrientation

    def getMiddleSplitLine(self, splitLines):
        priority = splitLines[0].priority
        n = 0
        while n < len(splitLines) and splitLines[n].priority == priority:
            n += 1

        return splitLines[int(n / 2)]

    def sortSplitLines(self, splitLines):
        splitLines.sort(key=lambda s: (s.priority, s.sortOrder))


def makeBSPTreeBuilder(resolver):
    return BSPTreeBuilder(resolver.resolve(SplitLineBuilder))
