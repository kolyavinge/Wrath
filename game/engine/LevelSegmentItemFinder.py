from game.engine.bsp.BSPTreeTraversal import BSPTreeTraversal


class LevelSegmentItemFinder:

    def __init__(self, traversal):
        self.traversal = traversal

    def getItemLevelSegments(self, bspTree, itemStartPoint, itemEndPoint):
        step = itemEndPoint.getCopy()
        step.sub(itemStartPoint)
        step.setLength(0.1)
        startPoint = itemStartPoint.getCopy()
        startPoint.add(step)
        endPoint = itemEndPoint.getCopy()
        endPoint.sub(step)
        startSegment = self.traversal.findLevelSegmentOrNone(bspTree, startPoint)
        endSegment = self.traversal.findLevelSegmentOrNone(bspTree, endPoint)
        assert startSegment is not None
        assert endSegment is not None
        itemLevelSegments = []
        self.findRec(bspTree, startPoint, endPoint, startSegment, endSegment, itemLevelSegments)

        return itemLevelSegments

    def findRec(self, bspTree, startPoint, endPoint, startSegment, endSegment, itemLevelSegments):
        if startSegment == endSegment:
            if startSegment not in itemLevelSegments:
                itemLevelSegments.append(startSegment)
        else:
            middlePoint = endPoint.getCopy()
            middlePoint.sub(startPoint)
            middlePoint.div(2)
            if middlePoint.getLength() > 0.1:
                middlePoint.add(startPoint)
                middleSegment = self.traversal.findLevelSegmentOrNone(bspTree, middlePoint)
                assert middleSegment is not None
                self.findRec(bspTree, startPoint, middlePoint, startSegment, middleSegment, itemLevelSegments)
                self.findRec(bspTree, middlePoint, endPoint, middleSegment, endSegment, itemLevelSegments)


def makeLevelSegmentItemFinder(resolver):
    return LevelSegmentItemFinder(resolver.resolve(BSPTreeTraversal))
