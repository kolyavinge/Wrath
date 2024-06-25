from game.engine.LevelSegmentItemFinder import LevelSegmentItemFinder


class LevelSegmentFloorAnalyzer:

    def __init__(self, segmentItemFinder):
        self.segmentItemFinder = segmentItemFinder

    def analyzeFloors(self, level):
        for floor in level.floors:
            self.analyzeDirection(level.bspTree, floor, floor.downLeft, floor.upRight)
            self.analyzeDirection(level.bspTree, floor, floor.upLeft, floor.downRight)

    def analyzeDirection(self, bspTree, floor, startPoint, endPoint):
        levelSegments = self.segmentItemFinder.getItemLevelSegments(bspTree, startPoint, endPoint)
        for levelSegment in levelSegments:
            assert levelSegment.floor is None or levelSegment.floor == floor
            levelSegment.floor = floor


def makeLevelSegmentFloorAnalyzer(resolver):
    return LevelSegmentFloorAnalyzer(resolver.resolve(LevelSegmentItemFinder))
