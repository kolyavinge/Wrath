from game.engine.bsp.BSPTreeTraversal import BSPTreeTraversal


class LevelSegmentItemFinder:

    def __init__(self, traversal: BSPTreeTraversal):
        self.traversal = traversal

    def findItemOrNone(self, bspTree, startSegment, endSegment, startPoint, endPoint, getFindItemResult):
        if startSegment == endSegment:
            return getFindItemResult(startSegment, startPoint, endPoint)
        else:
            direction = startPoint.getDirectionTo(endPoint)
            if direction.getLength() < 1.0:
                return getFindItemResult(startSegment, startPoint, endPoint) or getFindItemResult(endSegment, startPoint, endPoint)
            else:
                direction.div(2)
                middlePoint = startPoint.copy()
                middlePoint.add(direction)
                middleSegment = self.traversal.findLevelSegmentOrNone(bspTree, middlePoint)
                assert middleSegment is not None
                return self.findItemOrNone(
                    bspTree,
                    startSegment,
                    middleSegment,
                    startPoint,
                    middlePoint,
                    getFindItemResult,
                ) or self.findItemOrNone(
                    bspTree,
                    middleSegment,
                    endSegment,
                    middlePoint,
                    endPoint,
                    getFindItemResult,
                )
