class BSPTreeTraversal:

    def findLevelSegmentOrNone(self, bspTree, point):
        self.point = point
        self.findedLevelSegment = None
        self.findLevelSegmentRec(bspTree.root)

        return self.findedLevelSegment

    def findLevelSegmentRec(self, node):
        if node is None:
            self.findedLevelSegment = None
        elif node.isLeaf():
            self.findedLevelSegment = node.levelSegment
        else:
            pointDirection = self.point.getCopy()
            pointDirection.sub(node.basePoint)
            dotProduct = node.frontNormal.dotProduct(pointDirection)
            if dotProduct >= 0:
                self.findLevelSegmentRec(node.front)
            else:
                self.findLevelSegmentRec(node.back)


def makeBSPTreeTraversal(resolver):
    return BSPTreeTraversal()
