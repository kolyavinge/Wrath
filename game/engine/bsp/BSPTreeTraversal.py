class BSPTreeTraversal:

    def findLevelSegmentOrNone(self, bspTree, point):
        self.point = point
        self.findedLevelSegment = None
        self.findLevelSegmentRec(bspTree.root)

        return self.findedLevelSegment

    def findLevelSegmentRec(self, node):
        if node is None:
            self.findedLevelSegment = None
        elif node.isLeaf:
            self.findedLevelSegment = node.levelSegment
        else:
            if self.toFront(node):
                self.findLevelSegmentRec(node.front)
            else:
                self.findLevelSegmentRec(node.back)

    def toFront(self, node):
        x = self.point.x - node.basePoint.x
        y = self.point.y - node.basePoint.y
        z = self.point.z - node.basePoint.z
        dotProduct = x * node.frontNormal.x + y * node.frontNormal.y + z * node.frontNormal.z

        return dotProduct >= 0
