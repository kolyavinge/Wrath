from game.engine.bsp.SplitBorder import SplitBorder
from game.engine.bsp.SplitBorderBuilder import SplitBorderBuilder
from game.engine.bsp.SplitLineBuilder import SplitLineBuilder
from game.engine.bsp.SplitLinePosition import SplitLinePosition
from game.model.level.BSPTree import BSPNode
from game.model.level.LevelSegment import LevelSegment
from game.model.level.Orientation import Orientation


class BSPTreeBuilder:

    def __init__(self, splitLineBuilder, splitBorderBuilder):
        self.splitLineBuilder = splitLineBuilder
        self.splitBorderBuilder = splitBorderBuilder

    def build(self, level):
        splitBorder = self.getInitSplitBorder(level)
        splitLines = self.splitLineBuilder.getSplitLines(level)
        self.buildRec(level.bspTree.root, splitLines[0].orientation, splitBorder, splitLines)

    def getInitSplitBorder(self, level):
        maxX = 0
        maxY = 0
        maxZ = max([f.height for f in level.floors])
        for floor in level.floors:
            maxX = max(maxX, max([w.getMaxX() for w in floor.walls]))
            maxY = max(maxY, max([w.getMaxY() for w in floor.walls]))

        return SplitBorder(0, maxX, 0, maxY, 0, maxZ)

    def buildRec(self, node, splitOrientation, splitBorder, allSplitLines):
        splitLines = [s for s in allSplitLines if s.orientation == splitOrientation]
        if not splitLines:
            splitLines = allSplitLines.copy()
        splitLines.sort(key=lambda s: (s.priority, s.sortOrder))
        middleSplitLine = self.getMiddleSplitLine(splitLines)
        allSplitLines.remove(middleSplitLine)
        node.basePoint = middleSplitLine.startPoint
        node.frontNormal = middleSplitLine.frontNormal
        frontSplitLines, backSplitLines = self.getFrontAndBackSplitLines(allSplitLines, node.basePoint, node.frontNormal)
        newSplitOrientation = self.getNewSplitOrientation(splitOrientation, middleSplitLine)
        frontSplitBorder = self.splitBorderBuilder.getFrontSplitBorder(splitBorder, node.basePoint, node.frontNormal)
        if frontSplitBorder.isValid():
            node.front = BSPNode()
            if frontSplitLines:
                self.buildRec(node.front, newSplitOrientation, frontSplitBorder, frontSplitLines)
            else:
                node.front.levelSegment = LevelSegment.makeFromSplitBorder(frontSplitBorder)
        backSplitBorder = self.splitBorderBuilder.getBackSplitBorder(splitBorder, node.basePoint, node.frontNormal)
        if backSplitBorder.isValid():
            node.back = BSPNode()
            if backSplitLines:
                self.buildRec(node.back, newSplitOrientation, backSplitBorder, backSplitLines)
            else:
                node.back.levelSegment = LevelSegment.makeFromSplitBorder(backSplitBorder)

    def getMiddleSplitLine(self, splitLines):
        priority = splitLines[0].priority
        n = 0
        while n < len(splitLines) and splitLines[n].priority == priority:
            n += 1

        return splitLines[int(n / 2)]

    def getFrontAndBackSplitLines(self, splitLines, basePoint, frontNormal):
        front = []
        back = []
        for splitLine in splitLines:
            position = self.getSplitLinePosition(splitLine, basePoint, frontNormal)
            if position == SplitLinePosition.frontBack:
                front.append(splitLine)
                back.append(splitLine)
            elif position == SplitLinePosition.front:
                front.append(splitLine)
            elif position == SplitLinePosition.back:
                back.append(splitLine)
            else:  # SplitLineFrontBackPosition.parallel
                pass  # ignore this split line

        return (front, back)

    def getSplitLinePosition(self, splitLine, basePoint, frontNormal):
        direction = splitLine.startPoint.getCopy()
        direction.sub(basePoint)
        dotProductStart = direction.dotProduct(frontNormal)

        direction = splitLine.endPoint.getCopy()
        direction.sub(basePoint)
        dotProductEnd = direction.dotProduct(frontNormal)

        if dotProductStart == 0 and dotProductEnd == 0:
            dotProductNormal = splitLine.frontNormal.dotProduct(frontNormal)
            if dotProductNormal == 1 or dotProductNormal == -1:
                return SplitLinePosition.parallel

        if dotProductStart >= 0 and dotProductEnd >= 0:
            return SplitLinePosition.front

        if dotProductStart < 0 and dotProductEnd < 0:
            return SplitLinePosition.back

        if dotProductStart * dotProductEnd < 0:
            return SplitLinePosition.frontBack

        return SplitLinePosition.back

    def getNewSplitOrientation(self, splitOrientation, middleSplitLine):
        if middleSplitLine.orientationCanChange:
            return Orientation.getOpposite(splitOrientation)
        else:
            return splitOrientation


def makeBSPTreeBuilder(resolver):
    return BSPTreeBuilder(resolver.resolve(SplitLineBuilder), resolver.resolve(SplitBorderBuilder))
