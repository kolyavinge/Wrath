from game.engine.bsp.BSPTreeTraversal import BSPTreeTraversal
from game.lib.sys import warn


class LevelSegmentJoinLineAnalyzer:

    def __init__(self, traversal: BSPTreeTraversal):
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
            else:
                warn("JoinLine has no front and back segments.")

    def removeEmptyJoinLines(self, level):
        level.joinLines = [x for x in level.joinLines if x.frontLevelSegment is not None and x.backLevelSegment is not None]
