from game.engine.LevelSegmentItemFinder import (
    LevelSegmentItemFinder,
    VectorItemPointsSource,
)


class LevelSegmentWallAnalyzer:

    def __init__(self, segmentItemFinder):
        self.segmentItemFinder = segmentItemFinder

    def analyzeWalls(self, level, bspTree):
        for wall in level.walls:
            self.analyzeDirection(bspTree, wall, wall.startPoint, wall.endPoint)
            self.analyzeDirection(bspTree, wall, wall.upStartPoint, wall.endPoint)
            self.analyzeDirection(bspTree, wall, wall.startPoint, wall.upEndPoint)
            self.analyzeDirection(bspTree, wall, wall.upStartPoint, wall.upEndPoint)

    def analyzeDirection(self, bspTree, wall, startPoint, endPoint):
        levelSegments = self.segmentItemFinder.getItemLevelSegments(bspTree, VectorItemPointsSource(startPoint, endPoint))
        for levelSegment in levelSegments:
            levelSegment.walls.append(wall)


def makeLevelSegmentWallAnalyzer(resolver):
    return LevelSegmentWallAnalyzer(resolver.resolve(LevelSegmentItemFinder))
