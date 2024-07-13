from game.engine.bsp.BSPTreeTraversal import BSPTreeTraversal


class LevelSegmentJoinLineAnalyzer:

    def __init__(self, traversal):
        self.traversal = traversal

    def analyzeJoinLines(self, level, bspTree):
        for joinLine in level.joinLines:
            point = joinLine.middlePoint.getCopy()

            point.add(joinLine.frontNormal)
            frontLevelSegment = self.traversal.findLevelSegmentOrNone(bspTree, point)
            assert frontLevelSegment is not None
            frontLevelSegment.joinLines.append(joinLine)

            point.sub(joinLine.frontNormal)
            point.sub(joinLine.frontNormal)
            backLevelSegment = self.traversal.findLevelSegmentOrNone(bspTree, point)
            assert backLevelSegment is not None
            backLevelSegment.joinLines.append(joinLine)


def makeLevelSegmentJoinLineAnalyzer(resolver):
    return LevelSegmentJoinLineAnalyzer(resolver.resolve(BSPTreeTraversal))
