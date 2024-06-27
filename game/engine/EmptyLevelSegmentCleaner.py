class EmptyLevelSegmentCleaner:

    def clean(self, bspTree):
        self.cleanRec(None, bspTree.root)

    def cleanRec(self, parentNode, node):
        if node is None:
            return

        if node.isLeaf():
            assert node.levelSegment is not None
            if node.levelSegment.isEmpty():
                if node == parentNode.front:
                    parentNode.front = None
                else:
                    parentNode.back = None
        else:
            self.cleanRec(node, node.front)
            self.cleanRec(node, node.back)


def makeEmptyLevelSegmentCleaner(resolver):
    return EmptyLevelSegmentCleaner()
