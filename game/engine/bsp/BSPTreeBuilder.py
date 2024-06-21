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
        for floor in level.floors:
            maxX = max([w.getMaxX() for w in floor.walls])
            maxY = max([w.getMaxY() for w in floor.walls])
            maxZ = max([f.height for f in level.floors])
            splitBorder = SplitBorder(0, maxX, 0, maxY, 0, maxZ)
            splitLines = self.splitLineBuilder.getSplitLines(level)
            self.buildRec(floor.bspTree.root, splitLines[0].orientation, splitBorder, splitLines)

    def buildRec(self, node, splitOrientation, splitBorder, allSplitLines):
        splitLines = [s for s in allSplitLines if s.orientation == splitOrientation]
        splitLines.sort(key=lambda s: (s.priority, s.sortOrder))
        middleSplitLine = self.getMiddleSplitLine(splitLines)
        allSplitLines.remove(middleSplitLine)
        node.basePoint = middleSplitLine.startPoint
        node.frontNormal = middleSplitLine.frontNormal
        frontSplitLines, backSplitLines = self.getFrontAndBackSplitLines(allSplitLines, node.basePoint, node.frontNormal)
        newSplitOrientation = self.getNewSplitOrientation(splitOrientation, middleSplitLine)
        node.front = BSPNode()
        splitBorder = self.splitBorderBuilder.getFrontSplitBorder(splitBorder, node.basePoint, node.frontNormal)
        if frontSplitLines:
            self.buildRec(node.front, newSplitOrientation, splitBorder, frontSplitLines)
        else:
            node.front.levelSegment = LevelSegment.makeFromSplitBorder(splitBorder)
        if backSplitLines:
            node.back = BSPNode()
            splitBorder = self.splitBorderBuilder.getBackSplitBorder(splitBorder, node.basePoint, node.frontNormal)
            self.buildRec(node.back, newSplitOrientation, splitBorder, backSplitLines)

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

        if dotProductStart >= 0 and dotProductEnd >= 0:
            return SplitLinePosition.front

        if dotProductStart < 0 and dotProductEnd < 0:
            return SplitLinePosition.back

        if dotProductStart * dotProductEnd < 0:
            return SplitLinePosition.frontBack

        if dotProductStart == 0 and dotProductEnd == 0:
            dotProductNormal = splitLine.frontNormal.dotProduct(frontNormal)
            if dotProductNormal == 1 or dotProductNormal == -1:
                return SplitLinePosition.parallel

        return SplitLinePosition.back

    def getNewSplitOrientation(self, splitOrientation, middleSplitLine):
        if middleSplitLine.orientationCanChange:
            return Orientation.getOpposite(splitOrientation)
        else:
            return splitOrientation


def makeBSPTreeBuilder(resolver):
    return BSPTreeBuilder(resolver.resolve(SplitLineBuilder), resolver.resolve(SplitBorderBuilder))
