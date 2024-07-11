from game.anx.Constants import Constants
from game.engine.bsp.SplitBorder import SplitBorder
from game.engine.bsp.SplitBorderBuilder import SplitBorderBuilder
from game.engine.bsp.SplitLineBuilder import SplitLineBuilder
from game.engine.bsp.SplitLinePosition import SplitLinePosition
from game.model.level.BSPTree import BSPNode
from game.model.level.LevelSegment import LevelSegment


class BSPTreeBuilder:

    def __init__(self, splitLineBuilder, splitBorderBuilder):
        self.splitLineBuilder = splitLineBuilder
        self.splitBorderBuilder = splitBorderBuilder

    def build(self, bspTree, splitLines):
        splitBorder = SplitBorder(0, Constants.maxLevelSize, 0, Constants.maxLevelSize, 0, Constants.maxLevelSize)
        splitLines.sort(key=lambda s: (s.priority, s.sortOrder))
        self.buildRec(bspTree.root, splitBorder, splitLines)

    def buildRec(self, node, splitBorder, splitLines):
        middleSplitLine = self.getMiddleSplitLine(splitLines)
        splitLines.remove(middleSplitLine)
        node.basePoint = middleSplitLine.startPoint
        node.frontNormal = middleSplitLine.frontNormal
        frontSplitLines, backSplitLines = self.getFrontAndBackSplitLines(splitLines, node.basePoint, node.frontNormal)
        frontSplitBorder = self.splitBorderBuilder.getFrontSplitBorder(splitBorder, node.basePoint, node.frontNormal)
        if frontSplitBorder.isValid():
            node.front = BSPNode()
            if frontSplitLines:
                self.buildRec(node.front, frontSplitBorder, frontSplitLines)
            else:
                node.front.levelSegment = LevelSegment.makeFromSplitBorder(frontSplitBorder)
        backSplitBorder = self.splitBorderBuilder.getBackSplitBorder(splitBorder, node.basePoint, node.frontNormal)
        if backSplitBorder.isValid():
            node.back = BSPNode()
            if backSplitLines:
                self.buildRec(node.back, backSplitBorder, backSplitLines)
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


def makeBSPTreeBuilder(resolver):
    return BSPTreeBuilder(resolver.resolve(SplitLineBuilder), resolver.resolve(SplitBorderBuilder))
