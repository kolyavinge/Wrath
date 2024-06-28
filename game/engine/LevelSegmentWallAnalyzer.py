from game.engine.LevelSegmentItemFinder import LevelSegmentItemFinder


class LevelSegmentWallAnalyzer:

    def __init__(self, segmentItemFinder):
        self.segmentItemFinder = segmentItemFinder

    def analyzeWalls(self, level, bspTree):
        for wall in level.walls:
            levelSegments = self.segmentItemFinder.getItemLevelSegments(bspTree, wall.startPoint, wall.endPoint)
            for levelSegment in levelSegments:
                levelSegment.walls.append(wall)


def makeLevelSegmentWallAnalyzer(resolver):
    return LevelSegmentWallAnalyzer(resolver.resolve(LevelSegmentItemFinder))
