class BSPTreeTraversal:

    def findLevelSegmentOrNone(self, bspTree, point):
        self.point = point
        self.findedLevelSegment = None
        self.findLevelSegmentRec(bspTree.root)

        return self.findedLevelSegment

    def findLevelSegmentRec(self, parentNode):
        if parentNode is None:
            self.findedLevelSegment = None
        elif parentNode.isLeaf():
            self.findedLevelSegment = parentNode.levelSegment
        else:
            pointDirection = self.point.getCopy()
            pointDirection.sub(parentNode.basePoint)
            dotProduct = parentNode.frontNormal.dotProduct(pointDirection)
            if dotProduct >= 0:
                self.findLevelSegmentRec(parentNode.front)
            else:
                self.findLevelSegmentRec(parentNode.back)


def makeBSPTreeTraversal(resolver):
    return BSPTreeTraversal()
