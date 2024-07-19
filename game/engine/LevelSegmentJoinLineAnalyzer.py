from game.engine.bsp.BSPTreeTraversal import BSPTreeTraversal


class LevelSegmentJoinLineAnalyzer:

    def __init__(self, traversal):
        self.traversal = traversal

    def analyzeJoinLines(self, level, bspTree):
        self.findFrontBackLevelSegments(level, bspTree)
        self.removeEmptyJoinLines(level)

    def findFrontBackLevelSegments(self, level, bspTree):
        for joinLine in level.joinLines:
            point = joinLine.middlePoint.copy()

            point.add(joinLine.frontNormal)
            frontLevelSegment = self.traversal.findLevelSegmentOrNone(bspTree, point)
            assert frontLevelSegment is not None

            point.sub(joinLine.frontNormal)
            point.sub(joinLine.frontNormal)
            backLevelSegment = self.traversal.findLevelSegmentOrNone(bspTree, point)
            assert backLevelSegment is not None

            if frontLevelSegment != backLevelSegment:
                joinLine.frontLevelSegment = frontLevelSegment
                joinLine.backLevelSegment = backLevelSegment
                frontLevelSegment.joinLines.append(joinLine)
                backLevelSegment.joinLines.append(joinLine)

    def removeEmptyJoinLines(self, level):
        level.joinLines = [x for x in level.joinLines if x.frontLevelSegment is not None and x.backLevelSegment is not None]


def makeLevelSegmentJoinLineAnalyzer(resolver):
    return LevelSegmentJoinLineAnalyzer(resolver.resolve(BSPTreeTraversal))
