from game.engine.bsp.SplitLinePosition import SplitLinePosition
from game.model.level.BSPTree import BSPNode
from game.model.level.LevelSegment import LevelSegment


class BSPTreeBuilder:

    def build(self, bspTree, splitLines):
        splitLines.sort(key=lambda s: (s.priority, s.sortOrder))
        self.buildRec(bspTree.root, splitLines)

    def buildRec(self, node, splitLines):
        middleSplitLine = self.getMiddleSplitLine(splitLines)
        splitLines.remove(middleSplitLine)
        node.basePoint = middleSplitLine.startPoint
        node.frontNormal = middleSplitLine.frontNormal
        frontSplitLines, backSplitLines = self.getFrontAndBackSplitLines(splitLines, node.basePoint, node.frontNormal)
        node.front = BSPNode()
        if frontSplitLines:
            self.buildRec(node.front, frontSplitLines)
        else:
            node.front.isLeaf = True
            node.front.levelSegment = LevelSegment()
        node.back = BSPNode()
        if backSplitLines:
            self.buildRec(node.back, backSplitLines)
        else:
            node.back.isLeaf = True
            node.back.levelSegment = LevelSegment()

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
        direction = splitLine.startPoint.getDirectionTo(basePoint)
        dotProductStart = direction.dotProduct(frontNormal)

        direction = splitLine.endPoint.getDirectionTo(basePoint)
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
    return BSPTreeBuilder()
