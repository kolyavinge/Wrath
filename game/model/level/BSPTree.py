class BSPNode:

    def __init__(self):
        self.front = None
        self.back = None
        self.basePoint = None
        self.frontNormal = None
        self.levelSegment = None
        self.isLeaf = False


class BSPTree:

    def __init__(self):
        self.root = BSPNode()

    def getAllLevelSegments(self):
        segments = []
        self.getAllLevelSegmentsRec(self.root, segments)

        return segments

    def getAllLevelSegmentsRec(self, node, segments):
        if node.isLeaf:
            segments.append(node.levelSegment)
        else:
            self.getAllLevelSegmentsRec(node.front, segments)
            if node.back is not None:
                self.getAllLevelSegmentsRec(node.back, segments)
