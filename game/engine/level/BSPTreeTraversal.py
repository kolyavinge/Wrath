class BSPTreeTraversal:

    def findLevelSegment(self, bspTree, point):
        self.point = point
        self.findedLevelSegment = None
        self.findLevelSegmentRec(bspTree.root)

        return self.findedLevelSegment

    def findLevelSegmentRec(self, parentNode):
        if parentNode == None:
            self.findedLevelSegment = None
        elif parentNode.isLeaf():
            self.findedLevelSegment = parentNode.levelSegment
        else:
            pointDirection = self.point.getCopy()
            pointDirection.sub(parentNode.basePoint)
            if parentNode.frontNormal.dotProduct(pointDirection) >= 0:
                self.findLevelSegmentRec(parentNode.front)
            else:
                self.findLevelSegmentRec(parentNode.back)
