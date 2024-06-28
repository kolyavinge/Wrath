from game.engine.LevelSegmentItemFinder import LevelSegmentItemFinder


class LevelSegmentFloorAnalyzer:

    def __init__(self, segmentItemFinder):
        self.segmentItemFinder = segmentItemFinder

    def analyzeFloors(self, level, bspTree):
        for floor in level.floors:
            self.analyzeDirection(bspTree, floor, floor.downLeft, floor.upRight)
            self.analyzeDirection(bspTree, floor, floor.upLeft, floor.downRight)

            direction = floor.upRight.getCopy()
            direction.sub(floor.downLeft)
            direction.setLength(0.1)

            from1 = floor.downLeft.getCopy()
            from1.add(direction)
            self.analyzeDirection(bspTree, floor, from1, floor.upLeft)
            self.analyzeDirection(bspTree, floor, from1, floor.downRight)

            from1 = floor.upRight.getCopy()
            from1.sub(direction)
            self.analyzeDirection(bspTree, floor, from1, floor.upLeft)
            self.analyzeDirection(bspTree, floor, from1, floor.downRight)

    def analyzeDirection(self, bspTree, floor, startPoint, endPoint):
        levelSegments = self.segmentItemFinder.getItemLevelSegments(bspTree, startPoint, endPoint)
        for levelSegment in levelSegments:
            if floor not in levelSegment.floors:
                levelSegment.floors.append(floor)


def makeLevelSegmentFloorAnalyzer(resolver):
    return LevelSegmentFloorAnalyzer(resolver.resolve(LevelSegmentItemFinder))
