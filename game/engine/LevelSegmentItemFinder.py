from game.engine.bsp.BSPTreeTraversal import BSPTreeTraversal


class VectorItemPointsSource:

    def __init__(self, startPoint, endPoint):
        self.startPoint = startPoint.copy()
        self.endPoint = endPoint.copy()
        step = self.startPoint.getDirectionTo(self.endPoint)
        step.setLength(0.1)
        self.startPoint.add(step)
        self.endPoint.sub(step)

    def getStartPoint(self):
        return self.startPoint

    def getEndPoint(self):
        return self.endPoint

    def getMiddlePointOrNone(self, startPoint, endPoint):
        middlePoint = startPoint.getDirectionTo(endPoint)
        middlePoint.div(2)
        if middlePoint.getLength() > 0.1:
            middlePoint.add(startPoint)
            return middlePoint
        else:
            return None


class LevelSegmentItemFinder:

    def __init__(self, traversal):
        self.traversal = traversal

    def getItemLevelSegments(self, bspTree, itemPointsSource):
        startPoint = itemPointsSource.getStartPoint()
        endPoint = itemPointsSource.getEndPoint()
        startSegment = self.traversal.findLevelSegmentOrNone(bspTree, startPoint)
        endSegment = self.traversal.findLevelSegmentOrNone(bspTree, endPoint)
        itemLevelSegments = set()
        self.findRec(bspTree, startPoint, endPoint, itemPointsSource, startSegment, endSegment, itemLevelSegments)

        return itemLevelSegments

    def findRec(self, bspTree, startPoint, endPoint, itemPointsSource, startSegment, endSegment, itemLevelSegments):
        if startSegment is None and endSegment is None:
            return
        elif startSegment == endSegment:
            itemLevelSegments.add(startSegment)
        else:
            middlePoint = itemPointsSource.getMiddlePointOrNone(startPoint, endPoint)
            if middlePoint is not None:
                middleSegment = self.traversal.findLevelSegmentOrNone(bspTree, middlePoint)
                self.findRec(bspTree, startPoint, middlePoint, itemPointsSource, startSegment, middleSegment, itemLevelSegments)
                self.findRec(bspTree, middlePoint, endPoint, itemPointsSource, middleSegment, endSegment, itemLevelSegments)


def makeLevelSegmentItemFinder(resolver):
    return LevelSegmentItemFinder(resolver.resolve(BSPTreeTraversal))
