from game.engine.LevelSegmentItemFinder import LevelSegmentItemFinder


class LevelSegmentCeilingAnalyzer:

    def __init__(self, segmentItemFinder):
        self.segmentItemFinder = segmentItemFinder

    def analyzeCeilings(self, level, bspTree):
        for ceiling in level.ceilings:
            downLeft = ceiling.downLeft.getCopy()
            downLeft.add(ceiling.frontNormal)
            upRight = ceiling.upRight.getCopy()
            upRight.add(ceiling.frontNormal)
            self.analyzeDirection(bspTree, ceiling, downLeft, upRight)

    def analyzeDirection(self, bspTree, ceiling, startPoint, endPoint):
        levelSegments = self.segmentItemFinder.getItemLevelSegments(bspTree, startPoint, endPoint)
        for levelSegment in levelSegments:
            if ceiling not in levelSegment.ceilings:
                levelSegment.ceilings.append(ceiling)


def makeLevelSegmentCeilingAnalyzer(resolver):
    return LevelSegmentCeilingAnalyzer(resolver.resolve(LevelSegmentItemFinder))
