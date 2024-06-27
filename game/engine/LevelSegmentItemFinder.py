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
        itemLevelSegments = []
        self.findRec(bspTree, startPoint, endPoint, startSegment, endSegment, itemLevelSegments)

        return itemLevelSegments

    def findRec(self, bspTree, startPoint, endPoint, startSegment, endSegment, itemLevelSegments):
        if startSegment is None and endSegment is None:
            return
        elif startSegment == endSegment:
            if startSegment not in itemLevelSegments:
                itemLevelSegments.append(startSegment)
        else:
            middlePoint = endPoint.getCopy()
            middlePoint.sub(startPoint)
            middlePoint.div(2)
            if middlePoint.getLength() > 0.1:
                middlePoint.add(startPoint)
                middleSegment = self.traversal.findLevelSegmentOrNone(bspTree, middlePoint)
                self.findRec(bspTree, startPoint, middlePoint, startSegment, middleSegment, itemLevelSegments)
                self.findRec(bspTree, middlePoint, endPoint, middleSegment, endSegment, itemLevelSegments)


def makeLevelSegmentItemFinder(resolver):
    return LevelSegmentItemFinder(resolver.resolve(BSPTreeTraversal))
