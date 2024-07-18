from game.engine.LevelSegmentItemFinder import LevelSegmentItemFinder


class FloorPointsSource:

    def __init__(self, floor, startPoint, endPoint):
        self.floor = floor
        self.startPoint = startPoint.getCopy()
        self.endPoint = endPoint.getCopy()
        step = self.endPoint.getDirectionTo(self.startPoint)
        step.setLength(0.1)
        self.startPoint.add(step)
        self.endPoint.sub(step)
        self.startPoint.z = self.floor.getZ(self.startPoint.x, self.startPoint.y)
        self.endPoint.z = self.floor.getZ(self.endPoint.x, self.endPoint.y)

    def getStartPoint(self):
        return self.startPoint

    def getEndPoint(self):
        return self.endPoint

    def getMiddlePointOrNone(self, startPoint, endPoint):
        middlePoint = endPoint.getDirectionTo(startPoint)
        middlePoint.div(2)
        if middlePoint.getLength() > 0.5:
            middlePoint.add(startPoint)
            middlePoint.z = self.floor.getZ(middlePoint.x, middlePoint.y)
            return middlePoint
        else:
            return None


class LevelSegmentFloorAnalyzer:

    def __init__(self, segmentItemFinder):
        self.segmentItemFinder = segmentItemFinder

    def analyzeFloors(self, level, bspTree):
        for floor in level.floors:
            self.analyzeDirection(bspTree, floor, floor.downLeft, floor.upRight)
            self.analyzeDirection(bspTree, floor, floor.upLeft, floor.downRight)

            direction = floor.upRight.getDirectionTo(floor.downLeft)
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
        levelSegments = self.segmentItemFinder.getItemLevelSegments(bspTree, FloorPointsSource(floor, startPoint, endPoint))
        for levelSegment in levelSegments:
            if floor not in levelSegment.floors:
                levelSegment.floors.append(floor)


def makeLevelSegmentFloorAnalyzer(resolver):
    return LevelSegmentFloorAnalyzer(resolver.resolve(LevelSegmentItemFinder))
